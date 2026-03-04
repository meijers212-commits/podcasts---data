from confluent_kafka import Consumer
from consumptionconfig import ConsumptionConfig
import logging

config = ConsumptionConfig()

class ConsumptionConsumer:

    def __init__(self, config):

        self.config = config

        self.logger = logging.getLogger(self.__class__.__name__)

        self.consumer = None

        # try:
        self.logger.info("starting consumer")

        self.consumer = Consumer(self.config.KAFKA_CONF)
        self.consumer.subscribe([config.CONSUMER_TOPIC])
        self.logger.info("consumer Started")

        # except Exception as e:
        #     self.logger.error(f"ERROR occurred while Starting consumer: {e}")
        #     raise e

    def get_consumer(self):
        return self.consumer

    def close_consumer(self) -> None:
        self.logger.info("closeing consumer ...")
        self.consumer.close()
        self.logger.info("consumer closd")


a = ConsumptionConsumer(config=config)

b = a.get_consumer()