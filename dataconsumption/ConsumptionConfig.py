import os


class ConsumptionConfig:

    def __init__(self):

        self.BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
        self.CONSUMER_TOPIC = os.getenv("CONSUMER_TOPIC", "wav-metadata")
        self.conf = {"bootstrap.servers": self.BOOTSTRAP_SERVERS}
