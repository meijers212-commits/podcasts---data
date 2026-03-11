import os


class AnalizerConfig:

    def __init__(self):

        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "kafka:29092")

        self.CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "wav-metadata")

        self.CONSUMER_GROUP_ID = os.getenv("CONSUMER_GROUP_ID", "podcasts_anlays")

        self.PUBLISHER_TOPIC = os.getenv("PUBLISHER_TOPIC", "analys_text")

        self.KAFKA_CONF = {
            "bootstrap.servers": self.BOOTSTRAP_SERVERS,
            "group.id": self.CONSUMER_GROUP_ID,
            "auto.offset.reset": "earliest",
        }


config = AnalizerConfig()