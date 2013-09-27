from google.appengine.ext import db

# Create your models here.

class Encrypt(db.Model):
	client_ip = db.StringProperty()    
    request_date = db.DateTimeProperty()
    email = db.StringProperty()
    times = db.IntegerProperty()
    last = db.DateTimeProperty()
    create_ip = db.StringProperty()
    last_login_ip = db.StringProperty()