from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'travel_user'

    user_id = db.Column(db.String(30), primary_key=True, unique=True)
    user_name = db.Column(db.String(30))
    profile_url = db.Column(db.String(100))
    created = db.Column(db.DateTime)

    def __init__(self, user_id, user_name, profile_url):
        self.user_id = user_id
        self.user_name = user_name
        self.profile_url = profile_url
        self.created = datetime.now()


    def __repr__(self):
        return 'user_id : %s, user_name : %s, profile_url : %s' % (self.user_id, self.user_name, self.profile_url)