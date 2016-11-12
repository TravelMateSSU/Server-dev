from app import app
from app import db
from flask import request

@app.route('/event/enroll', methods=['POST'])
def enroll_event():
    to_client = dict()
    from_client = request.json
    print("사용자가 이벤트를 등록하려고 합니다. 우선 코스정보가 서버에 등록되어 있는 코스인지 확인합니다")
