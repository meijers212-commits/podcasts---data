from elasticsearch import Elasticsearch
import logging
from elasticsearch.helpers import bulk


class ElasticsearchClient:

    def __init__(self, config):

        self.config = config

        self.logger = logging.getLogger(self.__class__.__name__)

        self.es_client = Elasticsearch(self.config.ES_URI)

        # Get Document API
        if self.es_client.indices.exists(index=self.config.ES_INDEX):
            self.es_client.indices.delete(index=self.config.ES_INDEX)

        mapping = {
            "mappings": {
                "properties": {
                    "file_name": {"type": "keyword"},
                    "file_size": {"type": "integer"},
                    "file_size_in_MB": {"type": "integer"},
                    "create_time": {"type": "text"},
                }
            }
        }

        self.es_client.indices.create(index=self.config.ES_INDEX, body=mapping)

        if self.es_client.indices.exists(index=self.config.ES_INDEX):
            self.logger.info(f"index: {self.config.ES_INDEX} created and redy!")

    def index_record(self, record):

        res = self.es_client.index(
            index=self.config.ES_INDEX, id=record.get("id", ""), document=record
        )

        self.logger.info(f"record indexed with id: {res['_id']}")

    def index_many_records(self, actions: list[dict]):

        self.es_client.bulk(index=self.config.ES_INDEX, actions=actions)
        
        self.logger.info(f"{len(actions)} records indexed successfully")
