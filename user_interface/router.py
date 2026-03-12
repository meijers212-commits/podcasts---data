from fastapi import APIRouter, HTTPException
from dal import ElasticQueris
from router_schemas import AdminQuery
from interface_config import UserConfig
from shared.logging.logger import Logger
from shared.elasticserch.elasticserch_client import ElasticsearchClient

logger = Logger.get_logger(name="user_interface")

config = UserConfig(logger=logger)

es = ElasticsearchClient(
    logger=logger, elastic_uri=config.ES_URI, elastic_index=config.ES_INDEX
)

client = es.es_client

queris = ElasticQueris(
    config=config, logger=logger, es_index=config.ES_INDEX, client=client
)

router = APIRouter()


# 1
@router.get("/top_bds_percent/")
def get_top_percentes(count):

    res = queris.get_top_bds_percent(count=count)

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res


# 2
@router.get("/serch_by_word/")
def query_by_word(word):

    res = queris.serch_by_word(word=word)

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res


# 3
@router.get("/get_by_bds_threat_level/")
def query_by_thereat_level(threat_level):

    res = queris.get_by_bds_threat_level(threat_level)

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res


# 4
@router.get("/admin_free_query/")
def admin_free_query(ditalis: AdminQuery):

    res = queris.admain_query(ditalis.user_name, ditalis.password, ditalis.query)

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res


# 5
@router.get("/get_all_bds_by_size/")
def get_bds_by_size(size: int):

    res = queris.get_all_bds_by_size(size)

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res


# 6
@router.get("/get_count_of_etch_threat_level/")
def count_of_etch_threat_level():

    res = queris.get_count_of_etch_threat_level()

    if not res:
        raise HTTPException(status_code=404, detail=f"no result found,")

    return res
