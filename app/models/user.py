from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'travel_user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

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

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class UserBag(db.Model):
    """
    item_type = 1 : user_id <-> event_id 대응, 유저가 어떤 이벤트에 참여중인건지
    """
    __tablename__ = "user_bag"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    pid = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = db.Column(db.String(30))
    item_type = db.Column(db.Integer)               # 어떤 종류의 정보인지
    event_id = db.Column(db.Integer)                # 유저가 등록한 이벤트를 저장하는 용도
    created = db.Column(db.DateTime)

    def __init__(self, user_id, item_type, event_id):
        self.user_id = user_id
        self.item_type = item_type
        self.event_id = event_id
        self.created = datetime.now()

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}