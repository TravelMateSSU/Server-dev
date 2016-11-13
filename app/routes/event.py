from app import app
from app import db
from flask import request
from app.jobs.course import check_course_id, add_course

@app.route('/event/enroll', methods=['POST'])
def enroll_event():
    to_client = dict()
    from_client = request.json
    print("사용자가 이벤트를 등록하려고 합니다. 우선 코스정보가 서버에 등록되어 있는 코스인지 확인합니다")
    course_id = check_course_id(from_client['course_list'])
    print("course_id", course_id)
    if course_id:
        # course_id 가 존재한다는 것은 기존에 이미 같은 코스로 분류되는 정보가 존재하는 것
        # course_id 를 그대로 사용하면 된다
        print("기존에 존재하던 코스입니다")
        pass
    else:
        # 만약 course_id 가 존재하지 않는다면 해당 코스로 새로운 course_id 를 추가해주아야 한다
        print("새로운 코스를 등록합니다")
        add_course(None)
        pass

    return "something db processing done"