import collections
import pymongo
from pymongo import MongoClient

class GitResponseRepo:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb+srv://Anantha_sn:Anantha_sn@cluster0.kyfuw.mongodb.net/test?retryWrites=true&w=majority")
    def save_response(self, data: dict) -> bool:
        db = self.client.get_database('test')
        collections = db['image']
        id = collections.insert_one(data).inserted_id
        return True if id else False
