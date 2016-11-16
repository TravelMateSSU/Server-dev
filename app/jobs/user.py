from app import db
from app.models.event import TravelEvent
from app.models.user import UserBag
from app.jobs.event import search_event_by_eventid

def user_join_event(user_id, event_id):
    """
    유저가 이벤트에 참여하는 행동을 합니다
    """
    new_user_bag = UserBag(user_id, 1, event_id)
    db.session.add(new_user_bag)
    db.session.commit()
    print(user_id, " 의 UserBag 에 ", event_id, " 를 추가했습니다")
    event = search_event_by_eventid(event_id)
    current_tourist = event.current_tourist
    if current_tourist + 1 <= event.max_tourist:
        event.current_tourist=(event.current_tourist+1)
        db.session.commit()
        return True
    else:
        # 이미 모집인원이 꽉차버림..
        return False