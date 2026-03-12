import os
import sys

class AnalizerConfig:

    def __init__(self, logger):

        self.logger = logger

        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "kafka:29092")

        self.CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "wav-metadata")

        self.CONSUMER_GROUP_ID = os.getenv("CONSUMER_GROUP_ID", "podcasts_anlays")

        self.PUBLISHER_TOPIC = os.getenv("PUBLISHER_TOPIC", "analys_text")

        self.KAFKA_CONF = {
            "bootstrap.servers": self.BOOTSTRAP_SERVERS,
            "group.id": self.CONSUMER_GROUP_ID,
            "auto.offset.reset": "earliest",
        }

        self.validate()

    def validate(self):

        required_vars = {
            "BOOTSTRAP_SERVERS": self.BOOTSTRAP_SERVERS,
            "CONSUMER_TOPIC": self.CONSUMER_TOPIC,
            "CONSUMER_GROUP_ID": self.CONSUMER_GROUP_ID,
            "PUBLISHER_TOPIC": self.PUBLISHER_TOPIC,
        }

        missing = []

        for name, value in required_vars.items():
            if value is None or value.strip() == "":
                missing.append(name)

        if missing:
            self.logger.error(f"Necessary environment variables are missing to run the service: {missing}")
            sys.exit(1)

        self.logger.info("All variables have been loaded and are ready to use.")

