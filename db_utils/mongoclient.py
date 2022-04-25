from pymongo import MongoClient
import os, logging


class DB_Client:
    def __init__(self, database="population"):
        self.database = database
        self.config = {
            "username": os.getenv("MONGO_USER", ""),
            "password": os.getenv("MONGO_PASSWORD", ""),
            "server": os.getenv("MONGO_SERVER", ""),
            "port": os.getenv("MONGO_PORT", 27017),
        }
        self.connection()

    def connection(self):
        try:
            url = f"mongodb://{self.config['username']}:{self.config['passwords']}@localhost:{self.config['port']}/{self.database}"
            logging.info("Trying to connect to mongo...")
            self.db = MongoClient(url)
        except Exception as e:
            logging.info(f"Error: {e}")
            return None

    def insert_one(self, collection, values_dict: dict):
        if self.db is None:
            logging.info("Database connection is not working")
            return
        logging.info("Inserting one record")
        result = self.db[collection].insert_one(values_dict)
        print(result)
        return result

    def get_all_data(self, collection, values_dict=dict(), lookups=list()):
        if self.db is None:
            logging.info("Database connection is not working")
            return
        lookups_queries = self.lookup_unwind_formating(lookups)
        return self.db[collection].aggregate(
            [
                *lookups_queries,
                {"$match": values_dict},
            ]
        )

    def get_data(self, collection, values_dict=dict(), lookups=list()):
        lookups_queries = self.lookup_unwind_formating(lookups)
        data = self.db[collection].aggregate(
            [
                *lookups_queries,
                {
                    "$match": values_dict,
                },
                {
                    "$limit": 1,
                },
            ]
        )
        data = list(data)
        if not len(data):
            return None
        return data[0]

    def update_data(self, collection, values_dict, update_dict):
        return self.db[collection].update_one(values_dict, {"$set": update_dict})

    def delete_data(self, collection, values_dict):
        return self.db[collection].delete_one(values_dict)
