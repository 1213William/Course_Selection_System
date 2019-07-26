from lib import common
from core import model
from interface import student_interface, school_interface, course_interface


user_info = {
    'name': None,
}


def register():
    while 1:
        user_name = input('user_name:>>').strip()
        if user_name == 'q':
            break
        password = input('password:>>').strip()
        again_password = input('again_password:>>').strip()
        if password != again_password:
            print('密码输入不一致，请重新输入...')
            continue

        flag, msg = student_interface.save_student(model.Student(user_name, password))
        if flag:
            print(msg)
            break


def login():
    while 1:
        user_name = input('user_name:>>').strip()
        if user_name == 'q':break
        password = input('password:>>').strip()
        flag, msg = student_interface.login_interface(user_name, password)
        if flag:
            user_info['name'] = user_name
            print(msg)
            break
        else:
            print(msg)


@common.login_auth
def choice_school():
    while 1:
        res = school_interface.check_all_school()
        print(res)
        choice_s = input('请输入要去的学校:>>').strip()
        if choice_s == 'q':break
        if choice_s not in res:continue
        flag, msg = school_interface.add_student(user_info['name'], choice_s)
        if flag:
            print(msg)
            break


@common.login_auth
def choice_course():
    while 1:
        res = course_interface.check_all_course()
        print(res)
        choice_s = input('请输入要读的课程:>>').strip()
        if choice_s == 'q': break
        if choice_s not in res: continue
        flag, msg = course_interface.add_student(user_info['name'], choice_s)
        if flag:
            print(msg)
            break


@common.login_auth
def check_score():
    msg = student_interface.check_score(user_info['name'])
    print(msg)


