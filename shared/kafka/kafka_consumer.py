from confluent_kafka import Consumer
import time

class KafkaConsumer:

    def __init__(self, logger, kafka_config, consumer_topic):

        self.logger = logger

        self.consumer = None

        try:

            logger.info("starting consumer")
            self.consumer = Consumer(kafka_config)
            logger.info("consumer started successfully...")

        except Exception as e:
            logger.exception(f"consumer activation failed., Error: {e}")

        try:

            while True:

                topics = self.consumer.list_topics(timeout=5)

                if consumer_topic in topics.topics:

                    logger.info(f'topic: {consumer_topic} found subscribing')

                    self.consumer.subscribe([consumer_topic])

                    logger.info(f'consumer subscribed to topic: {consumer_topic}')
                    self.logger.info("consumer Started")

                    break

                else:

                    logger.warning(f'topic: {consumer_topic} not found yet tring agen')
                    time.sleep(3)

        except Exception as e:
            logger.error(f'error getting topic list end subscribing, {e}')

    def get_consumer(self):
        return self.consumer

    def close_consumer(self) -> None:
        self.logger.info("closeing consumer ...")
        self.consumer.close()
        self.logger.info("consumer closd")

