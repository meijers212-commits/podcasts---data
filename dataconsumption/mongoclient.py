from pymongo import MongoClient
import logging


class MongoClient:

    def __init__(self, config):

        self.logger = logging.getLogger(self.__class__.__name__)

        self.config = config

        self.client = None

        try:

            self.client = MongoClient(self.config.MONGO_URI)
            self.logger.info("mongo client is redy !")

        except Exception as e:

            self.logger.info("ERROR occurred while creating mongo client")

            raise e

        self.client = self.get_mongo_client()

    def get_mongo_client(self):
        return self.client[self.config.MONGO_DB_NAME][self.config.MONGO_DB_COLLACTION]

    def insert_doc(self, doc: dict):

        self.client.insertOne(doc)

    def insert_many_docs(self, doc_list: list[dict]):

        self.client.insertMany(doc_list)
