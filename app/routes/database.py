from app import app
from flask import request, jsonify

@app.route('/db', methods=['GET'])
def show_db_inside():
    """
    개발용으로 사용하는 db 내용물을 보는 기능
    """
    to_client = dict()
    table_name = request.args.get('table_name')
    if table_name == 'travel_user':
        from app.models.user import User
        queries = User.query.all()
        to_client['debug'] = "user 테이블에 대한 쿼리의 결과입니다"
    elif table_name == 'travel_event':
        from app.models.event import TravelEvent
        queries = TravelEvent.query.all()
        to_client['debug'] = "event 테이블에 대한 쿼리의 결과입니다"
    elif table_name == 'course_meta':
        from app.models.course import CourseMeta
        queries = CourseMeta.query.all()
        to_client['debug'] = "course_meta 테이블에 대한 쿼리의 결과입니다"
    elif table_name == 'course_detail':
        from app.models.course import CourseDetail
        queries = CourseDetail.query.all()
        to_client['debug'] = 'course_detail 테이블에 대한 쿼리의 결과입니다'
    else:
        to_client['debug'] = '테이블 이름을 잘못 입력하셨습니다. table_name 필드에 travel_user, travel_event, course_meta, course_detail 을 입력해주세요'
        return jsonify(to_client)

    to_client['queries'] = list()
    for each_query in queries:
        to_client['queries'].append(each_query.as_dict())

    return jsonify(to_client)