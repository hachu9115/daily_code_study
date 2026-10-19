def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for i in range(len(db)):
        if (id_pw[0] in db[i]) & (id_pw[1] not in db[i]):
            return "wrong pw"
    return "fail"