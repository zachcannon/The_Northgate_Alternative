from google.appengine.ext import db

class RecommenderUser(db.Model):
	username = db.StringProperty(required = True)
