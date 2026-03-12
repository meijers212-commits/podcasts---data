from shared.logging.logger import Logger
from analizer_config import AnalizerConfig
from text_analysis import Analizer
import json
from shared.kafka.kafka_consumer import KafkaConsumer
from shared.kafka.kafka_producer import KafkaPublisher

logger = Logger.get_logger(name="text_analyzer")


def run():
    
    config = AnalizerConfig(logger=logger)

    analizer_consumer = KafkaConsumer(
        logger=logger,
        kafka_config=config.KAFKA_CONF,
        consumer_topic=config.CONSUMER_TOPIC
    )

    publisher = KafkaPublisher(
        logger=logger,
        bootstrap_service=config.BOOTSTRAP_SERVERS,
        publisher_topic=config.PUBLISHER_TOPIC,
        client_id="text_analizer"
    )

    consumer = analizer_consumer.get_consumer()

    analizer = Analizer(logger=logger)

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

                logger.info(f"processing wav: {data.get('file_name', '')}")

                object = analizer.bds_percent(data)

                publisher.publish(object)

                logger.info(f"doc 📄: {data.get('file_name', '')} - sent to kafka")

            except Exception as e:
                logger.error(f"Error occurred {e}")
                continue

    finally:
        consumer.unsubscribe()
        consumer.close()
        publisher.flush()

run()