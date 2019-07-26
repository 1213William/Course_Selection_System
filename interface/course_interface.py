from db import db_handler
from conf import settings


def save_course(dic):
    db_handler.save(settings.BASE_COURSE, dic)
    return True, '课程创建成功...'


def check_all_course():
    res = db_handler.select_all(settings.BASE_COURSE)
    new_res = []
    for i in res:
        n = i.split('.')
        new_res.append(n[0])
    return new_res


def add_student(name, course):
    dic = db_handler.select(settings.BASE_COURSE, course)
    dic.add_to_student(name)
    db_handler.save(settings.BASE_COURSE, dic)
    return True, '课程选择成功...'


def add_teacher(course, name):
    dic = db_handler.select(settings.BASE_TEACHER, name)
    dic.add_to_course(course)
    db_handler.save(settings.BASE_TEACHER, dic)
    return True, '课程选择完成...'


def check_course_student(course):
    dic = db_handler.select(settings.BASE_COURSE, course)
    return dic.student



if __name__ == '__main__':
    print(check_all_course())

