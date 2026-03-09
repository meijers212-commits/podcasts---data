from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError
from logger import logger

class ElasticsearchClient:

    def __init__(self, config):

        self.config = config

        self.logger =logger

        self.es_client = Elasticsearch(self.config.ES_URI)
        
        if not self.es_client.indices.exists(index=self.config.ES_INDEX):
           logger.warning(f'cant rech index: {self.config.ES_INDEX}')

        if self.es_client.indices.exists(index=self.config.ES_INDEX):
            self.logger.info(f"index: {self.config.ES_INDEX} found and ready!")

        


    




    