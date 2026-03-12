from consumption_config import config
import json
from shared.logging.logger import Logger
from shared.kafka.kafka_consumer import KafkaConsumer
from shared.mongo.mongo_client import MongoConnection
from shared.elasticserch.elasticserch_client import ElasticsearchClient

logger = Logger.get_logger(name="data_consumption")


def run():

    consum = KafkaConsumer(
        logger=logger,
        kafka_config=config.KAFKA_CONF,
        consumer_topic=config.CONSUMER_TOPIC,
    )

    consumer = consum.get_consumer()

    mongo = MongoConnection(
        logger=logger,
        mongo_uri=config.MONGO_URI,
        mongo_db=config.MONGO_DB_NAME,
        mongo_collection=config.MONGO_COLLACTION,
    )

    es = ElasticsearchClient(
        logger=logger, 
        elastic_uri=config.ES_URI, 
        elastic_index=config.ES_INDEX
    )

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

                data["id"] = str(hash(data["file_name"]))

                mongo.insert_doc(data)

                if "_id" in data:
                    del data["_id"]

                es.index_record(data)

                logger.info(
                    f"doc 📄: {data.get('file_name', '')} - inserted to mongodb"
                )

            except Exception as e:
                logger.error(f"Error occurred {e}")
                raise e

    finally:
        consumer.unsubscribe()
        consumer.close()


run()
