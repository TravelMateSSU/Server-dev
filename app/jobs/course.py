from app import db
from app.models.course import CourseDetail, CourseMeta
from sqlalchemy import and_

def check_course_id(course_list):
    """
    course_list 에 담아져 있는 코스정보 하나하나를 뽑아서, 현재 존재하는 코스 정보 중에서 겹치는 course_id 가 있는지 탐색한다
    만약 존재하면 해당 course_id 를 리턴하고
    만약 존재하지 않는다면 새로운 course_id 를 course_meta table 에 생성하고 course_detail table 에 코스의 자세한 정보를 등록한다.
    또한 새롭게 만들어지는 course_id 를 리턴한다.
    코스의 컨텐츠와 sequence_id 가 같으면 같은 코스라고 인식한다
    """
    course_set = set()                                          # 예상 course_id set
    content_id_list = [x['content_id'] for x in course_list]     # course_list 에서 content_id 값들만 뽑아놓은 리스트
    content_sequence_list = [x['sequence_id'] for x in course_list]

    for item in course_list:
        queries = CourseDetail.query.filter(and_(CourseDetail.content_id == item['content_id'],
                                                 CourseDetail.sequence_id == item['sequence_id'])).all()
        for each_query in queries:
            course_set.add(each_query.course_id)

    # 이렇게 하고 나면 course_set 에는 후보가 될 course_id 들이 중복없이 들어가게 된다
    print("후보가 될 course_id : ", course_set)

    is_exist = False
    course_id = None
    for each_course_id in course_set:
        queries = CourseDetail.query.filter_by(course_id=each_course_id).all()
        temp_content_list = [x.content_id for x in queries]
        temp_content_sequence_list = [x.sequence_id for x in queries]

        if temp_content_list == content_id_list and temp_content_sequence_list == content_sequence_list:
            # 두개가 동일하다면, 컨텐츠가 동일하다는 것이므로 같은 코스로 인식한다
            is_exist = True
            course_id = each_course_id
            break
        else:
            # 두개가 동일하지 않다면 계속 진행한다
            continue

    if is_exist:
        # 이미 코스 정보가 존재한다면
        return course_id
    else:
        # 코스 정보가 기존에 존재하지 않는다면
        return None

def add_course(course_list):
    """
    새로운 코스정보를 추가하는 작업을 합니다
    새로운 코스정보를 추가하고 그 코스의 course_id 를 리턴합니다
    """
    new_course_meta = CourseMeta(1)
    db.session.add(new_course_meta)
    db.session.commit() # 새로운 CourseMeta row 추가 완료

    new_course_id = CourseMeta.query.order_by(CourseMeta.created.desc()).first().course_id
    for detail_item in course_list:
        new_course_detail = CourseDetail(new_course_id, detail_item['sequence_id'], detail_item['content_id'], detail_item['content_type'], detail_item['image_url'])
        db.session.add(new_course_detail)
        db.session.commit()

    return new_course_id