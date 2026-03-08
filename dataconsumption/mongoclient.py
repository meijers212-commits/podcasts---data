from pymongo import MongoClient
from logger import logger


class MongoConnection:

    def __init__(self, config):

        self.logger = logger

        self.config = config

        self.client = None

        try:

            self.client = MongoClient(self.config.MONGO_URI)
            self.client.admin.command('ping')
            self.logger.info("mongo client is ready !")

        except Exception as e:

            self.logger.info("ERROR occurred while creating mongo client")

            raise e

        self.collection = self.get_mongo_client()

    def get_mongo_client(self):
        return self.client[self.config.MONGO_DB_NAME][self.config.MONGO_DB_COLLACTION]

    def insert_doc(self, doc: dict):

        self.collection.insert_one(doc)

    def insert_many_docs(self, doc_list: list[dict]):

        self.collection.insert_many(doc_list)
