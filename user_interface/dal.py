from es_client import ElasticsearchClient
from interface_config import UserConfig
from logger import logger

config = UserConfig()

es = ElasticsearchClient(config)

client = es.es_client


class ElasticQueris:

    def __init__(self, config):

        self.config = config

        self.es_index = self.config.ES_INDEX

        self.client = es.es_client

    # 1
    def get_top_bds_percent(self, count):

        query = {
            "size": count,
            "query": {"match_all": {}},
            "sort": [{"bds_percent": {"order": "desc"}}],
        }

        response = self.client.search(index=self.es_index, body=query)
        return response["hits"]["hits"]

    # 2
    def serch_by_word(self, word):

        query = {"query": {"match": {"file_text": word}}}

        response = self.client.search(index=self.es_index, body=query)
        return response["hits"]["hits"]

    # 3
    def get_by_bds_threat_level(self, threat_level):

        query = {"query": {"match": {"bds_threat_level": threat_level}}}

        response = self.client.search(index=self.es_index, body=query)
        return response["hits"]["hits"]

    # 4
    def admain_query(self, user_name, password, query):

        try:
            if (
                user_name == self.config.ADMIN_USER_NAME
                and password == self.config.ADMIN_PASSWORD
            ):
                response = self.client.search(index=self.es_index, body=query)

                if not response["hits"]["hits"]:
                    return {"message": "No results found for your query"}
                
                return response["hits"]["hits"]

            else:
                return {"Error": f"Unauthorized user {user_name}"}
            
        except Exception as e:
            logger.error(f'error while processing admin query, Error: {e}')

            return {f"Error while processing query. Check syntax": {e}}

    # 5
    def get_all_bds_by_size(self,size):
        
        max_size = 10000

        query = {"size":min(size, max_size),
                 "query": {
            "term": {
                "is_bds": True
                }
            }
        }

        response = self.client.search(index=self.es_index, body=query)
        return response["hits"]["hits"]
    

    # 6
    def get_count_of_etch_threat_level(self):

        query = {"size": 0,
                    "aggs": {
                    "bds_threat_level_count": {
                    "terms": { "field": "bds_threat_level" }
                    }
                }
                }

        response = self.client.search(index=self.es_index, body=query)
        return response["aggregations"]["bds_threat_level_count"]["buckets"]
    

    

