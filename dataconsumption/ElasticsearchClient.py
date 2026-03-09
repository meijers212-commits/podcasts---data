from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError
from logger import logger

class ElasticsearchClient:

    def __init__(self, config):

        self.config = config

        self.logger =logger

        self.es_client = Elasticsearch(self.config.ES_URI)

        mapping = {
            "mappings": {
                "properties": {
                    "file_name": {"type": "keyword"},
                    "file_size": {"type": "integer"},
                    "file_size_in_MB": {"type": "integer"},
                    "create_time": {"type": "text"},
                    "bds_percent": {"type": "integer"},
                    "is_bds": {"type": "boolean"},
                    "bds_threat_level": {"type": "keyword"},
                }
            }
        }

        
        if not self.es_client.indices.exists(index=self.config.ES_INDEX):
            self.es_client.indices.create(index=self.config.ES_INDEX, body=mapping)

        if self.es_client.indices.exists(index=self.config.ES_INDEX):
            self.logger.info(f"index: {self.config.ES_INDEX} created and ready!")

    def index_record(self, record):

        res = self.es_client.index(
            index=self.config.ES_INDEX, id=str(record.get("id", "")), document=record
        )

        self.logger.info(f"record indexed with id: {res['_id']}")

    def index_many_records(self, data: list[dict]):

        actions = [
            {
                "_index": self.config.ES_INDEX,
                "_id": doc["id"],
                "_source": {
                    "file_name": doc["file_name"],
                    "file_size": doc["file_size"],
                    "file_size_in_MB": doc["file_size_in_MB"],
                    "create_time": doc["create_time"],
                    "bds_percent": doc["bds_percent"],
                    "is_bds": doc["is_bds"],
                    "bds_threat_level": doc["bds_threat_level"],
                },
            }
            for doc in data
        ]

        try:

            bulk(self.es_client, actions)
            self.logger.info(f"Data successfully indexed in {self.config.ES_INDEX} index.")

        except BulkIndexError as e: 

            self.logger.error(f"Failed to index documents to '{self.config.ES_INDEX}':") 
            for err in e.errors:

                self.logger.error(err)
                
        self.logger.info(f"{len(actions)} records indexed successfully")
