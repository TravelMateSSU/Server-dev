from app import db
from app.models.event import TravelEvent

def add_new_event(new_event_object, course_id):
    new_event = TravelEvent(new_event_object['user_id'],
                            course_id,
                            new_event_object['title'],
                            new_event_object['description'],
                            new_event_object['max_tourist'],
                            new_event_object['start_time'],
                            new_event_object['end_time'],
                            new_event_object['event_end_time'],
                            new_event_object['hash_tag'])
    db.session.add(new_event)
    db.session.commit()

def search_events_by_userid(user_id):
    """
    user_id 를 기준으로 event 찾기, all 로 찾음
    """
    return TravelEvent.query.filter_by(user_id=user_id).all()

def search_events(status=1):
    """
    status = 1 : 현재 모집중인 event 만 보기
    status = 0 : 모집 종료된 event 만 보기
    status = -1 : 모든 event 보기
    """
    if status == -1:
        return TravelEvent.query.all()
    else:
        return TravelEvent.query.filter_by(status=status).all()