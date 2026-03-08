import os


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

        self.MONGO_DB_COLLACTION = os.getenv("MONGO_DB_COLLACTION", "podcasts_audio")