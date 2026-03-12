from confluent_kafka import Producer
import json


class KafkaPublisher:

    def __init__(self, logger, bootstrap_service, publisher_topic, client_id):

        self.publisher_topic = publisher_topic

        self.logger = logger

        self.conf = {
            "bootstrap.servers": bootstrap_service,
            "client.id": client_id,
        }

        try:

            logger.info("starting Publisher...")
            self.producer = Producer(self.conf)
            logger.info("Publisher started successfully...")

        except Exception as e:
            logger.exception(f"Publisher activation failed, Error: {e}")

    def acked(self, err, msg):
        if err is not None:
            self.logger.info("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            self.logger.info("Message produced: %s" % (str(msg)))

    def publish(self, payload):

        self.producer.produce(
            self.publisher_topic,
            value=json.dumps(payload).encode("utf-8"),
            callback=self.acked,
        )

        self.producer.poll(1)

    def flush(self):
        self.producer.flush()
