import os


class ConsumptionConfig:

    def __init__(self):

        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")

        self.CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "wav-metadata")

        self.CONSUMER_GROUP_ID = os.getenv("CONSUMER_GROUP_ID", "podcasts_anlays")

        self.KAFKA_CONF = {
            "bootstrap.servers": self.BOOTSTRAP_SERVERS,
            "group.id": self.CONSUMER_GROUP_ID,
        }

        self.ES_URI = os.getenv("ES_URI", "http://localhost:9200")
        self.ES_INDEX = os.getenv("ES_INDEX", "podcasts")

        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "podcasts")

        self.MONGO_DB_COLLACTION = os.getenv("MONGO_DB_COLLACTION", "podcasts")