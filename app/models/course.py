from app import db
from datetime import datetime

class CourseMeta(db.Model):
    __tablename__ = 'course_meta'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    course_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    selected_num = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, selected_num):
        self.selected_num = selected_num
        self.created = datetime.now()

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class CourseDetail(db.Model):
    __tablename__ = 'course_detail'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    pid = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True) # primary key
    course_id = db.Column(db.Integer)                       # 어느 코스에 해당하는 내용물인지
    sequence_id = db.Column(db.Integer)                     # 해당 코스의 순서를 의미하는 칼럼
    content_id = db.Column(db.String(50), nullable=False)   # API 의 content_id 를 담아둘 칼럼, NOT NULL
    content_type = db.Column(db.String(20), nullable=False) # API 의 content_type 을 담아둘 칼럼, NOT NULL
    image_url = db.Column(db.String(200))                   # API 의 image url 정보를 담아둘 칼럼

    def __init__(self, course_id, sequence_id, content_id, content_type, image_url):
        self.course_id = course_id
        self.sequence_id = sequence_id
        self.content_id = content_id
        self.content_type = content_type
        self.image_url = image_url

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class CourseReview(db.Model):
    __tablename__ = 'course_review'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    pid = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)  # primary key
    course_id = db.Column(db.Integer)                       # 어느 코스에 해당하는 내용물인지
    user_id = db.Column(db.String(30))
    review = db.Column(db.String(1000))
    created = db.Column(db.DateTime)

    def __init__(self, course_id, user_id, review):
        self.course_id = course_id
        self.user_id = user_id
        self.review = review
        self.created = datetime.now()

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
