from es_client import ElasticsearchClient
from interface_config import UserConfig

config = UserConfig()

es = ElasticsearchClient(config)

client = es.es_client


class Elastic_queris:

    def __init__(self,config):
        
        self.es_index = config.ES_INDEX
        self.client = es.es_client

    def get_top_bds_percent(self, count):

        query = {
            "size": count,
            "query":{
                "math_all": {}
                },
                "sort": [
                    {"bds_percent": {"order": "desc"}}
                ]
            }
            
        return self.client.search(index=self.es_index, body=query)
    
    def serch_by_word(self,word):

        query = 


#    mapping = {
#             "mappings": {
#                 "properties": {
#                     "file_name": {"type": "keyword"},
#                     "file_size": {"type": "integer"},
#                     "file_size_in_MB": {"type": "integer"},
#                     "create_time": {"type": "text"},
#                     "bds_percent": {"type": "integer"},
#                     "is_bds": {"type": "boolean"},
#                     "bds_threat_level": {"type": "keyword"},
#                 }
#             }
#         }
