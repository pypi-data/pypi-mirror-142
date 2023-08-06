import asyncio
import os
from distutils.util import strtobool

import aio_pika
import httpx
import orjson
from aio_pika import DeliveryMode
from aio_pika.pool import Pool


async def run(loop, logger=None, config=None, consumer_pool_size=10):
    async def _get_connection():
        return await aio_pika.connect(
            host=config.get("mq_host"),
            port=config.get("mq_port"),
            login=config.get("mq_user"),
            password=config.get("mq_pass"),
            virtualhost=config.get("mq_vhost"),
            loop=loop
        )

    async def _send_to_dlq(content, channel):
        exchange = await channel.get_exchange(config.get("mq_dlq_exchange"))
        await exchange.publish(
            aio_pika.Message(content.encode('utf-8'), delivery_mode=DeliveryMode.PERSISTENT),
            config.get("mq_dlq_routing_key")
        )

    async def _send_to_solr(message, collection):
        message = orjson.loads(message)
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.get('solr_base_url')}/{collection}/update",
                json=message,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code != 200:
                raise Exception(
                    f"Solr error while indexing {message['id']}: {response.status_code} {response.text}")
            else:
                if logger:
                    logger.debug(f"Record indexed: {message['id']}")

    async def _get_channel():
        async with connection_pool.acquire() as connection:
            return await connection.channel()

    async def _consume(consumer_id):
        async with channel_pool.acquire() as channel:
            queue = await channel.declare_queue(
                config.get("mq_queue"), durable=config.get("mq_queue_durable"), auto_delete=False
            )
            while True:
                try:
                    m = await queue.get(timeout=300 * consumer_pool_size)
                    message = m.body.decode('utf-8')
                    collection = config.get('solr_collection') if config.get('solr_collection') else m.routing_key
                    try:
                        await _send_to_solr(message, collection)
                    except Exception as e:
                        logger.error(f"{str(e)}. Sending to DLQ")
                        await _send_to_dlq(message, channel)
                    finally:
                        await m.ack()
                except aio_pika.exceptions.QueueEmpty:
                    if logger:
                        logger.info("Consumer %s: Queue empty. Stopping." % consumer_id)
                    break

    if config is None:
        config = {
            "mq_host": os.environ.get('MQ_HOST'),
            "mq_port": int(os.environ.get('MQ_PORT', '5672')),
            "mq_vhost": os.environ.get('MQ_VHOST'),
            "mq_user": os.environ.get('MQ_USER'),
            "mq_pass": os.environ.get('MQ_PASS'),
            "mq_queue": os.environ.get('MQ_QUEUE'),
            "mq_dlq_exchange": os.environ.get('MQ_DLQ_EXCHANGE'),
            "mq_dlq_routing_key": os.environ.get("MQ_DLQ_ROUTING_KEY"),
            "mq_queue_durable": bool(strtobool(os.environ.get('MQ_QUEUE_DURABLE', 'True'))),
            "solr_base_url": os.environ.get('SOLR_BASE_URL'),
            "consumer_pool_size": os.environ.get("CONSUMER_POOL_SIZE"),
        }

    if "consumer_pool_size" in config:
        if config.get("consumer_pool_size"):
            try:
                consumer_pool_size = int(config.get("consumer_pool_size"))
            except TypeError as e:
                if logger:
                    logger.error("Invalid pool size: %s" % (consumer_pool_size,))
                raise e

    connection_pool = Pool(_get_connection, max_size=consumer_pool_size, loop=loop)
    channel_pool = Pool(_get_channel, max_size=consumer_pool_size, loop=loop)

    async with connection_pool, channel_pool:
        consumer_pool = []
        if logger:
            logger.info("Consumers started")
        for i in range(consumer_pool_size):
            consumer_pool.append(_consume(consumer_id=i))

        await asyncio.gather(*consumer_pool)
