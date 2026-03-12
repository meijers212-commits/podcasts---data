from pymongo import MongoClient

class MongoConnection:

    def __init__(self, logger, mongo_uri, db_name, collection_name=None):
        
        self.db_name = db_name

        self.collection_name = collection_name
        
        self.logger = logger

        self.client = None

        try:

            self.client = MongoClient(mongo_uri)
            self.client.admin.command('ping')
            self.logger.info("mongo client is ready !")

        except Exception as e:

            self.logger.exception(f"ERROR occurred while creating mongo client: {e}")

    def get_mongo_collection(self):
        return self.client[self.db_name][self.collection_name]

    def insert_doc(self, doc: dict):

        self.client[self.db_name][self.collection_name].insert_one(doc)

    def insert_many_docs(self, doc_list: list[dict]):

        self.client[self.db_name][self.collection_name].insert_many(doc_list)
