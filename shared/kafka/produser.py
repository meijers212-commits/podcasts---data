from confluent_kafka import Producer
import json

class KafkaPublisher:

    def __init__(self, config, logger):

        self.config = config

        self.logger = logger

        self.conf = {
            "bootstrap.servers": self.config.BOOTSTRAP_SERVERS,
            "client.id": "Ingestionservice",
        }

        self.producer = Producer(self.conf)

    def acked(self, err, msg):
        if err is not None:
            self.logger.info("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            self.logger.info("Message produced: %s" % (str(msg)))

    def publish(self, payload):

        self.producer.produce(
            self.config.PUBLISHER_TOPIC,
            value=json.dumps(payload).encode("utf-8"),
            callback=self.acked,
        )

        self.producer.poll(1)

    def flush(self):
        self.producer.flush()