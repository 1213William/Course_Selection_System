from db import db_handler
from conf import settings


def save_teacher(dic):
    db_handler.save(settings.BASE_TEACHER, dic)
    return True, '学校创建成功...'


def login_interface(name):
    dic = db_handler.select(settings.BASE_TEACHER, name)
    if dic:
        if dic.name == name:
            return True, '登陆成功...'
        else:
            return False, '用户名或密码错误...'
    return None, '当前用户不存在...'


