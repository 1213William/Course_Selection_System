from db import db_handler
from conf import settings


def save_student(dic):
    db_handler.save(settings.BASE_STUDENT, dic)
    return True, '学生创建成功...'


def login_interface(name, pwd):
    dic = db_handler.select(settings.BASE_STUDENT, name)
    if dic:
        if dic.name == name and dic.password == pwd:
            return True, '登陆成功...'
        else:
            return False, '用户名或密码错误...'
    return None


def check_score(name):
    dic = db_handler.select(settings.BASE_STUDENT, name)
    if dic.score:
        return dic.score
    return '当前老师还未登记成绩...'


def check_all_student():
    res = db_handler.select_all(settings.BASE_STUDENT)
    new_res = []
    for i in res:
        n = i.split('.')
        new_res.append(n[0])
    return new_res


def change_score(name, score):
    dic = db_handler.select(settings.BASE_STUDENT, name)
    dic.add_to_score(score)
    db_handler.save(settings.BASE_STUDENT, dic)
    return True, '成绩修改成功...'

