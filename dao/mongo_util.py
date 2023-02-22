import pymongo
client = pymongo.MongoClient("mongodb+srv://beercafeguy:beercafeguy@beercafecluster.5i7z0cc.mongodb.net/?retryWrites=true&w=majority")
db = client['crm']
    

def insert_reviews(reviews,collection_name):
    coll= db[collection_name]
    coll.insert_many(reviews)
