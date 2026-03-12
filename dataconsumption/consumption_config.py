import os
import sys
from consumption_orchestrator import logger


class ConsumptionConfig:

    def __init__(self):

        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "kafka:29092")

        self.CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "analys_text")

        self.CONSUMER_GROUP_ID = os.getenv("CONSUMER_GROUP_ID", "podcasts_saver")

        self.KAFKA_CONF = {
            "bootstrap.servers": self.BOOTSTRAP_SERVERS,
            "group.id": self.CONSUMER_GROUP_ID,
            "auto.offset.reset": "earliest",
        }

        self.ES_URI = os.getenv("ES_URI", "http://elasticserch:9200")
        self.ES_INDEX = os.getenv("ES_INDEX", "podcasts")

        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "podcasts")

        self.MONGO_COLLACTION = os.getenv("MONGO_DB_COLLACTION", "podcasts_audio")

        self.validate()

    def validate(self):

        required_vars = {
            "BOOTSTRAP_SERVERS": self.BOOTSTRAP_SERVERS,
            "CONSUMER_TOPIC": self.CONSUMER_TOPIC,
            "CONSUMER_GROUP_ID": self.CONSUMER_GROUP_ID,
            "ES_URI": self.ES_URI,
            "ES_INDEX": self.ES_INDEX,
            "MONGO_URI": self.MONGO_URI,
            "MONGO_DB_NAME": self.MONGO_DB_NAME,
            "MONGO_DB_COLLACTION": self.MONGO_COLLACTION,
        }

        missing = []

        for name, value in required_vars.items():
            if value is None or value.strip() == "":
                missing.append(name)

        if missing:
            logger.error(
                f"Necessary environment variables are missing to run the service: {missing}"
            )
            sys.exit(1)

        logger.info("All variables have been loaded and are ready to use.")


config = ConsumptionConfig()
