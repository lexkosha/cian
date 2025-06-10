import logging

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient('mongodb://lex:Sara2517!@92.63.103.198:27017/')


def db_mongo_insert_one(db_name: str, col_name: str, data: dict):
    try:
        db = client[db_name]
        collections = db[col_name].insert_one(data)
        return logging.info(f'Create document {collections} ')
    except DuplicateKeyError as dke:
        logging.info(dke)


def db_mongo_insert_many(db_name: str, col_name: str, data: list):
    try:
        db = client[db_name]
        collections = db[col_name].insert_many(data)
        return logging.info(f'Create document {collections} ')
    except DuplicateKeyError as dke:
        logging.info(dke)




def db_mongo_find(db_name: str, col_name: str, filter: dict, project: dict):
    max_time = 60000
    collections = client[db_name][col_name].find(
        filter=filter,
        projection=project,
        max_time_ms=max_time
    )
    return collections


def db_mongo_delete_many(db_name: str, col_name: str, filter: dict):
    collections = client[db_name][col_name].delete_many(
        filter=filter)
    logging.info(f'{collections.deleted_count}: объектов удалено!')


def return_ids_old():
    filter = {}
    project = {
        'point_id': 1
    }
    result = client['avitoPVZ']['point_id'].find(
        filter=filter,
        projection=project
    )
    return result