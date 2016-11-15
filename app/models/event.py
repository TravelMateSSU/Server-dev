from app import db
from datetime import datetime

class TravelEvent(db.Model):
    __tablename__ = 'travel_event'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    event_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True) # primary key for event table
    user_id = db.Column(db.String(30))          # 어느 사용자가 이벤트를 오픈했는지
    course_id = db.Column(db.Integer)           # 어느 코스를 사용하는지, 해당 코스의 detail 정보를 모두 가져올 수 있다
    title = db.Column(db.String(30))            # 해당 모집글의 제목정보
    description = db.Column(db.String(1000))    # 사용자가 작성할 이벤트의 설명글
    max_tourist = db.Column(db.Integer)         # 최대 모집자 수
    current_tourist = db.Column(db.Integer)     # 현재 모집자 수
    travel_start_time = db.Column(db.DateTime)  # 여행 시작 날짜와 시간
    travel_end_time = db.Column(db.DateTime)    # 여행 끝 날짜와 시간
    event_end_time = db.Column(db.DateTime)     # 모집이 끝나는 시간, 모집글이 등록되는 순간부터 모집 시
    status = db.Column(db.Integer)              # 모집여부, 0: 모집 끝, 1:모집 진행중
    hash_tag = db.Column(db.String(200))        # 검색을 위해서 이벤트가 지나가는 경로에 대한 해시태그
    created = db.Column(db.DateTime)

    def __init__(self, user_id, course_id, title, description, max_tourist, start_time, end_time, event_end_time, hash_tag):
        self.user_id = user_id
        self.course_id = course_id
        self.title = title
        self.description = description
        self.max_tourist = max_tourist
        self.current_tourist = 1            # 처음에는 무조건 본인 한명
        self.travel_start_time = start_time
        self.travel_end_time = end_time
        self.event_end_time = event_end_time
        self.status = 1                     # 처음에 등록하면 무조건 모집 중 상태
        self.hash_tag = hash_tag
        self.created = datetime.now()       # 만들면 현재 날짜를 등록

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

