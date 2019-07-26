from core import student



def teacher_login_auth(func):
    from core import teacher
    def inner(*args, **kwargs):
        if teacher.teacher_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            print('请先去登陆...')
    return inner


def login_auth(func):
    def wrapper(*args, **kwargs):
        if student.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            print('请先去登陆')
    return wrapper



