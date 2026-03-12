from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError

class ElasticsearchClient:

    def __init__(self, logger, elastic_uri, elastic_index):

        self.elastic_index = elastic_index

        self.logger = logger

        self.es_client = Elasticsearch(elastic_uri)

        mapping = {
            "mappings": {
                "properties": {
                    "file_name": {"type": "keyword"},
                    "file_size": {"type": "integer"},
                    "file_size_in_MB": {"type": "integer"},
                    "create_time": {"type": "text"},
                    "file_text": {"type": "text"},
                    "bds_percent": {"type": "integer"},
                    "is_bds": {"type": "boolean"},
                    "bds_threat_level": {"type": "keyword"},
                }
            }
        }

        
        if not self.es_client.indices.exists(index=elastic_index):
            self.es_client.indices.create(index=elastic_index, body=mapping)

        if self.es_client.indices.exists(index=elastic_index):
            self.logger.info(f"index: {elastic_index} created and ready!")

    def index_record(self, record):

        res = self.es_client.index(
            index=self.elastic_index, id=str(record.get("id", "")), document=record
        )

        self.logger.info(f"record indexed with id: {res['_id']}")

    def index_many_records(self, data: list[dict]):

        actions = [
            {
                "_index": self.elastic_index,
                "_id": doc["id"],
                "_source": {
                    "file_name": doc["file_name"],
                    "file_size": doc["file_size"],
                    "file_size_in_MB": doc["file_size_in_MB"],
                    "create_time": doc["create_time"],
                    "file_text": doc["file_text"],
                    "bds_percent": doc["bds_percent"],
                    "is_bds": doc["is_bds"],
                    "bds_threat_level": doc["bds_threat_level"],
                },
            }
            for doc in data
        ]

        try:

            bulk(self.es_client, actions)
            self.logger.info(f"Data successfully indexed in {self.elastic_index} index.")

        except BulkIndexError as e: 

            self.logger.error(f"Failed to index documents to '{self.elastic_index}':") 
            for err in e.errors:

                self.logger.error(err)
                
        self.logger.info(f"{len(actions)} records indexed successfully")
