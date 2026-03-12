from confluent_kafka import Consumer
import time



class ConsumptionConsumer:

    def __init__(self, config, logger):

        self.config = config

        self.logger = logger

        self.consumer = None

        self.logger.info("starting consumer")

        self.consumer = Consumer(self.config.KAFKA_CONF)

        try:

            while True:

                topics = self.consumer.list_topics(timeout=5)

                if config.CONSUMER_TOPIC in topics.topics:

                    logger.info(f'topic: {config.CONSUMER_TOPIC} found subscribing')

                    self.consumer.subscribe([config.CONSUMER_TOPIC])

                    logger.info(f'consumer subscribed to topic: {config.CONSUMER_TOPIC}')
                    self.logger.info("consumer Started")

                    break

                else:

                    logger.warning(f'topic: {config.CONSUMER_TOPIC} not found yet tring agen')
                    time.sleep(3)

        except Exception as e:
            logger.error(f'error getting topic list end subscribing, {e}')

    def get_consumer(self):
        return self.consumer

    def close_consumer(self) -> None:
        self.logger.info("closeing consumer ...")
        self.consumer.close()
        self.logger.info("consumer closd")

