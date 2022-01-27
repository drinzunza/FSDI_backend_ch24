import pymongo
import certifi

mongo_url = "mongodb+srv://student:FullStack110@cluster0.oosfc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())


# get the specific database
db = client.get_database("OrganikaStore")