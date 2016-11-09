from app import db
from datetime import datetime

class TravelEvent(db.Model):
    __tablename__ = 'travel_event'

    event_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True) # primary key for event table
    user_id = db.Column(db.String(30))          # 어느 사용자가 이벤트를 오픈했는지
    course_id = db.Column(db.Integer)           # 어느 코스를 사용하는지, 해당 코스의 detail 정보를 모두 가져올 수 있다
    description = db.Column(db.String(1000))    # 사용자가 작성할 이벤트의 설명글
    hash_tag = db.Column(db.String(200))        # 검색을 위해서 이벤트가 지나가는 경로에 대한 해시태그
    created = db.Column(db.DateTime)

    def __init__(self, user_id, course_id, description, hash_tag):
        self.user_id = user_id
        self.course_id = course_id
        self.description = description
        self.hash_tag = hash_tag

