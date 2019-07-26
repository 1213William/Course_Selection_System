from lib import common
from interface import course_interface, teacher_interface, student_interface


teacher_info = {
    'name': None
}


def login():
    while 1:
        user_name = input('user_name:>>').strip()
        flag, msg = teacher_interface.login_interface(user_name)
        if flag:
            teacher_info['name'] = user_name
            print(msg)
            break
        else:
            print(msg)


@common.teacher_login_auth
def check_course():
    res = course_interface.check_all_course()
    print(res)


@common.teacher_login_auth
def choice_course():
    while 1:
        res = course_interface.check_all_course()
        print(res)
        choice_c = input('请输入要选择的课程:>>').strip()
        if choice_c == 'q':break
        if choice_c not in res:continue
        flag, msg = course_interface.add_teacher(choice_c, teacher_info['name'])
        if flag:
            print(msg)
            break


@common.teacher_login_auth
def check_course_student():
    while 1:
        res = course_interface.check_all_course()
        print(res)
        choice_c = input('请输入要查看的课程:>>').strip()
        if choice_c == 'q':break
        if choice_c not in res:continue
        print(course_interface.check_course_student(choice_c))
        break


@common.teacher_login_auth
def change_student_score():
    while 1:
        res = student_interface.check_all_student()
        print(res)
        choice_s = input('请输入要修改的学生名称:>>').strip()
        if choice_s == 'q':break
        if choice_s not in res:continue
        score = input('请输入要修改的分数:>>').strip()
        flag, msg = student_interface.change_score(choice_s, score)
        if flag:
            print(msg)
            break
