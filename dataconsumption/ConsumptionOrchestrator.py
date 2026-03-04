from consumptionconfig import ConsumptionConfig
from consumptionconsumer import ConsumptionConsumer
import logging
import asyncio
import json
from mongoclient import MongoClient
from elasticsearchclient import ElasticsearchClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

config = ConsumptionConfig()

consumer = ConsumptionConsumer(config=config)

topics = config.CONSUMER_TOPIC

logger = logging.getLogger("Consumption Orchestrator")

mongo = MongoClient()

es = ElasticsearchClient()

def run():

    try:

        while True:

            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                logger.error(f"Kafka Error: {msg.error()}")
                continue

            try:
                data = json.loads(msg.value().decode("utf-8"))
                logger.info(f"Consumed wav: {data.get('file_name', '')}")
                
                data["id"] = hash(data["file_name"])

                es.index_record(data)
                
                mongo.insert_doc(data)
                logger.info(f'doc 📄: {data.get('file_name', '')} - inserted to mongodb')

            except Exception as e:
                logger.error(f"Error occurred {e}")
                raise e

            consumer.store_offsets(message=msg)

    finally:
        consumer.unsubscribe()
        consumer.close()


run()
