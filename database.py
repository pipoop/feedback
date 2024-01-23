import json
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")


def connect_2_db():
    # connect to mongo
    password = quote_plus(MONGODB_PASSWORD)
    url = f"mongodb+srv://{MONGODB_USERNAME}:{password}@cluster0.hm3ugvt.mongodb.net/{MONGODB_DB_NAME}?retryWrites=true&w=majority"

    client = MongoClient(url)
    db = client[MONGODB_DB_NAME]
    feedbacks = db["feedbacks"]
    

    return feedbacks


def save_feedback_to_db(feedback):
    feedbacks = connect_2_db()
    feedbacks.insert_one({"feedback": feedback})


# if __name__ == '__main__':
#   _,_ = connect_2_db()
