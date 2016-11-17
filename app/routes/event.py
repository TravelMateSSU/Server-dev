from app import app
from flask import request, jsonify
from app.jobs.course import check_course_id, add_course
from app.jobs.event import add_new_event, search_events_by_userid, search_events, search_events_by_hashtag
from app.jobs.user import user_join_event

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
        to_client['debug'] = "사용자가 기존에 존재하던 코스를 이용합니다"
        add_new_event(from_client, course_id)
        to_client['enroll_event'] = True
    else:
        # 만약 course_id 가 존재하지 않는다면 해당 코스로 새로운 course_id 를 추가해주아야 한다
        print("새로운 코스를 등록합니다")
        to_client['debug'] = "사용자가 기존에 없던 새로운 코스를 등록하여 사용합니다"
        new_course_id = add_course(from_client['course_list'])
        print("new course id : ", new_course_id)
        add_new_event(from_client, new_course_id)
        to_client['enroll_event'] = True

    return jsonify(to_client)

@app.route('/event/list', methods=['POST'])
def events_list():
    to_client = dict()
    to_client['events_list'] = list()

    from_client = request.json
    if from_client['status'] == 2:
        # 특정 아이디로 찾을 때
        queries = search_events_by_userid(from_client['user_id'])
        to_client['debug'] = "특정 사용자의 아이디로 모집글을 찾습니다"
        for open_events in queries:
            to_client['events_list'].append(open_events.as_dict())
    elif from_client['status'] == 3:
        # hash_tag 로 검색하는 경우가 들어올 것이다
        queries = search_events_by_hashtag(from_client['hash_tag'], from_client['offset'], from_client['limit'])
        to_client['debug'] = from_client['hash_tag']+" 의 키워드를 갖는 내용으로 이벤트 리스트를 찾은 결과입니다"
        for open_events in queries:
            to_client['events_list'].append(open_events.as_dict())
    else:
        # status 에 따라서 찾아갈 때
        # 1 : 모집중, 0 : 모집종료, -1: 모든 경우
        queries = search_events(from_client['status'], from_client['offset'], from_client['limit'])
        to_client['debug'] = "모집 상태에 따라서 모집글을 찾습니다"
        for open_events in queries:
            to_client['events_list'].append(open_events.as_dict())

    return jsonify(to_client)

@app.route('/event/join', methods=['POST'])
def join_event():
    to_client = dict()
    from_client = request.json

    if user_join_event(from_client['user_id'], from_client['event_id']):
        # join 에 성공하였다는 뜻
        to_client['debug'] = "해당 이벤트에 참여가 성공하였습니다 current_tourist 의 수가 업데이트 되었는지 확인해주세요"
        to_client['join_event'] = True
    else:
        # join 에 실패하였다는 뜻
        to_client['debug'] = "이벤트 참여에 실패하였습니다 모집인원이 꽉찼거나 알 수 없는 이유에 의해서 실패하였습니다"
        to_client['join_event'] = False

    return jsonify(to_client)