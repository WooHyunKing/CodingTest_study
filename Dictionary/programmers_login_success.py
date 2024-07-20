def solution(id_pw, db):
    answer = ''
    
    # 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"
    # 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”
    # 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw"
    
    db_dict = dict()
    
    for id, pw in db:
        db_dict[id] = pw
    
    if id_pw[0] not in db_dict:
        return "fail"
    else:
        if db_dict[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"