from pymongo import MongoClient

class MongoConnection:

    def __init__(self, logger, mongo_uri, mongo_db, mongo_collection):
        
        self.mongop_db = mongo_db

        self.mongo_collection = mongo_collection
        
        self.logger = logger

        self.client = None


        try:

            self.client = MongoClient(mongo_uri)
            self.client.admin.command('ping')
            self.logger.info("mongo client is ready !")

        except Exception as e:

            self.logger.exception(f"ERROR occurred while creating mongo client: {e}")

    def get_mongo_collection(self):
        return self.client[self.mongop_db][self.mongo_collection]

    def insert_doc(self, doc: dict):

        self.collection.insert_one(doc)

    def insert_many_docs(self, doc_list: list[dict]):

        self.collection.insert_many(doc_list)
