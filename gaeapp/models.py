from google.appengine.ext import db

# Create your models here.

class Encrypt(db.Model):
	client_ip = db.StringProperty()    
    request_date = db.DateTimeProperty()
    db = text.StringProperty()