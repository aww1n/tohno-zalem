from motor.motor_asyncio import AsyncIOMotorClient
import pymongo 
client = AsyncIOMotorClient('localhost',port = 27017)
db = client['activite_bot']
db_users = db['users']









sink_client = pymongo.MongoClient('localhost',port = 27017)
sink_db = sink_client['activite_bot']
sink_db_users = sink_db['users']



print(sink_db_users.find_one(filter={'id': 5122589211, "state":'wait new category'}))


