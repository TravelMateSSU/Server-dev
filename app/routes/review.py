from app import app
from flask import jsonify, request
from app.jobs.course import add_course_review, search_course_reviews

@app.route('/review/enroll', methods=['POST'])
def add_review():
    to_client = dict()
    from_client = request.json

    add_course_review(from_client['course_id'], from_client['user_id'], from_client['review'])
    to_client['debug'] = str(from_client['course_id'])+" 에 리뷰를 등록하였습니다"
    return jsonify(to_client)


@app.route('/review/list', methods=['POST'])
def show_review_list():
    to_client = dict()
    from_client = request.json

    to_client['review_list'] = list()
    queries = search_course_reviews(from_client['course_id'], from_client['offset'], from_client['limit'])
    for each_query in queries:
        to_client['review_list'].append(each_query.as_dict())

    return jsonify(to_client)