import json
from pymongo import MongoClient
import fetch_data

class MongoDataHandler:
    def __init__(self) -> None:
        f = open('./config.json')
        data = json.load(f)
        f.close()
        self.database = data["DATABASE"]
        self.client = MongoClient(data["MONGO_CON_STRING"])
    
    def save_response(self, data: dict, collection) -> bool:
        db = self.client.get_database(self.database)
        collections = db[collection]
        id = collections.insert_one(data).inserted_id
        return True if id else False

    def extract_user_data_from_issues(self):
        db = self.client.get_database(self.database)
        collection = db["Issue"].distinct("data.user_data")
        # print(collection)
        count=0
        for user in collection:
            login = user["login"]
            id = db['user'].find({"login": login}).distinct("login")
            print(id)
            if not id:
                db['user'].insert_one(user).inserted_id
                count+=1
        return count

    def extract_user_data_from_commits(self):
        db = self.client.get_database(self.database)
        collection = db["commit"].distinct("data.Author")
        # print(collection)
        count=0
        for c in collection:
            author_login = c.split("<")
            id = db['user'].find({"login": author_login}).distinct("login")
            if not id:
                user = fetch_data.fetch_git_data().get_user(author_login[0].strip())
                if not "message" in user.keys():
                    db['user'].insert_one(user)
                    count+=1
        return count
