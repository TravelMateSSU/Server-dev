from app import db
from app.models.course import CourseDetail

def check_course(course_list):
    """
    course_list 에 담아져 있는 코스정보 하나하나를 뽑아서, 현재 존재하는 코스 정보 중에서 겹치는 course_id 가 있는지 탐색한다
    만약 존재하면 해당 course_id 를 리턴하고
    만약 존재하지 않는다면 새로운 course_id 를 course_meta table 에 생성하고 course_detail table 에 코스의 자세한 정보를 등록한다.
    또한 새롭게 만들어지는 course_id 를 리턴한다.
    """
    pass