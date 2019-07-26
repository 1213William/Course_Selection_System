from db import db_handler
from conf import settings


def save_school(school):
    db_handler.save(settings.BASE_SCHOOL, school)
    return True, '学校创建成功'


def check_all_school():
    res = db_handler.select_all(settings.BASE_SCHOOL)
    new_res = []
    for i in res:
        n = i.split('.')
        new_res.append(n[0])
    return new_res


def add_teacher(t_name, t_school):
    dic = db_handler.select(settings.BASE_SCHOOL, t_school)
    dic.add_to_teacher(t_name)
    db_handler.save(settings.BASE_SCHOOL, dic)
    return '学校绑定成功...'


def add_student(name, school):
    dic = db_handler.select(settings.BASE_SCHOOL, school)
    dic.add_to_student(name)
    db_handler.save(settings.BASE_SCHOOL, dic)
    return True, '学校选择成功...'
