from fastapi import APIRouter, HTTPException
from dal import ElasticQueris
from logger import logger
from router_schemas import AdminQuery

queris = ElasticQueris()

router = APIRouter()


# 1
@router.get("/top_bds_percent/")
def get_top_percentes(count):

    try:

        return queris.get_top_bds_percent(count=count)

    except Exception as e:

        logger.error(e)
        raise HTTPException(status_code=402, detail=e)


# 2
@router.get("/serch_by_word/")
def query_by_word(word):

    try:

        return queris.serch_by_word(word=word)

    except Exception as e:

        logger.error(e)
        raise HTTPException(status_code=402, detail=e)


# 3
@router.get("/get_by_bds_threat_level/")
def query_by_thereat_level(threat_level):

    try:

        return queris.get_by_bds_threat_level(threat_level)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=402, detail=e)


# 4
@router.get("/admin_free_query/")
def admin_free_query(ditalis: AdminQuery):

    try:

        return queris.admain_query(ditalis.user_name, ditalis.password, ditalis.query)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=402, detail=e)


# 5
@router.get("/get_all_bds_by_size/")
def get_bds_by_size(size: int):

    try:

        return queris.get_all_bds_by_size(size)

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=402, detail=e)


# 6
@router.get("/get_count_of_etch_threat_level/")
def count_of_etch_threat_level():

    try:

        return queris.get_count_of_etch_threat_level()

    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=402, detail=e)
