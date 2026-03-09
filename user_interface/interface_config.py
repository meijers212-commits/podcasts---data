import os


class UserConfig:

    def __init__(self):

        self.ES_URI = os.getenv("ES_URI", "http://elasticserch:9200")
        self.ES_INDEX = os.getenv("ES_INDEX", "podcasts")