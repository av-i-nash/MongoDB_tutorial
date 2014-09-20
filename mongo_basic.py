from bottle import route, run, template
from pymongo import MongoClient

@route('/')
def index():
    connection = MongoClient("127.0.0.1", 27017)
    db = connection.test
    names = db.names
    item = names.find_one()
    return "Hello %s!!!" % item["name"]
   
run(host = "localhost", port = 8080) 
