import pymongo

mongo_url = "mongodb+srv://student:FullStack110@cluster0.oosfc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)


# get the specific database
db = client.get_database("OrganikaStore")