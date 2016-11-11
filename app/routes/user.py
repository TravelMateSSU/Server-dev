from app import app, db
from flask import request,jsonify
from app.models.user import User

@app.route('/user', methods=['POST'])
def enter_user():
    """
    사용자가 서비스에 로그인하기 위한 로직을 담습니다
    enroll_force : False 가 기본입니다
    True 로 들어오면 기존 가입여부를 확인하고, 가입되어 있지 않은 경우에만 가입후 자동 로그인을 수행합니다
    """
    to_clinet = dict()
    from_client = request.json
    if from_client['enroll_force'] == False:
        # 로그인 행위일 경우에
        user = User.query.filter_by(user_id=from_client['user_id']).first()
        if user:
            # 유저가 이미 등록되어 있다면
            to_clinet['login'] = True
            to_clinet['debug'] = "사용자는 서버에 정상 등록되어 있습니다. 회원정보롤 담아서 보냅니다."
            to_clinet['user_name'] = user.user_name
            to_clinet['profile_url'] = user.profile_url
        else:
            # 유저가 등록되어 있지 않다면
            to_clinet['login'] = False
            to_clinet['debug'] = "사용자는 서버에 등록되어 있지 않은 상태입니다. 등록하시겠습니까? enroll_force:True 로 재전송해주세요"
    else:
        # 회원가입 행위
        user = User.query.filter_by(user_id=from_client['user_id']).first()
        if user:
            # 이미 해당 아이디가 서버에 등록되어 있다면
            to_clinet['enroll'] = False
            to_clinet['login'] = False
            to_clinet['debug'] = "사용자는 서버에 이미 등록되어 있습니다. 중복된 아이디는 등록할 수 없습니다. enroll_force:False 로 재시도 해보세요."
        else:
            # 서버에 사용자가 등록되어 있지 않은 경우, 회원가입 시키고 로그인까지 시킨다
            new_user = User(from_client['user_id'], from_client['user_name'], from_client['profile_url'])
            print("다음 사용자를 회원가입 시도합니다", new_user)
            db.session.add(new_user)
            result = db.session.commit()
            if result is None:
                # result 에 None 이 오면 문제없이 들어가는 것 같음
                # 그래서 None 아니면 에러메세지를 뱉는거 아닌가 싶음
                to_clinet['enroll'] = True
                to_clinet['login'] = True
                to_clinet['debug'] = "사용자는 회원가입에 성공하였고 로그인을 허가합니다."
                to_clinet['user_name'] = from_client['user_name']
                to_clinet['profile_url'] = from_client['profile_url']
                print("사용자는 회원가입 성공하였습니다")
            else:
                # db insert query fail
                to_clinet['enroll'] = False
                to_clinet['login'] = False
                to_clinet['debug'] = "DB Insert 작업이 실패하였습니다"
                print("DB Insert 작업 오류로 회원가입에 실패하였습니다")
    print(to_clinet)
    return jsonify(to_clinet)