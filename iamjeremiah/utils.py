import pymongo 

def post_listing_all():
  db = pymongo.MongoClient('localhost', 27017)
  collection = db.flasktest.flasktest
  return collection.find()


def check_if_empty(title):
  db = pymongo.MongoClient('localhost', 27017)
  collection = db.flasktest.flasktest
  post = collection.find({'title': title})
  if post.count() == 0:
    return False
  else:
    return post
