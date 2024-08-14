def solution(id_pw, db):
    answer = ''
    newdb = {}
    for i in db:
        newdb[i[0]] = i[1]
    
    if id_pw[0] in newdb:
        if newdb[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"        
        
    return "fail"