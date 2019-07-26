from core import model
from interface import school_interface, teacher_interface, course_interface


def create_school():
    s_lst = ['shanghai', 'beijing']
    school = model.School
    while 1:
        s_name = input('请输入要创建的学校名称:>>').strip()
        if s_name == 'q':break
        if s_name not in s_lst:continue
        s_address = input('请输入学校的地址:>>').strip()
        if s_address == 'q':break
        flag, msg = school_interface.save_school(school(s_name, s_address))

        if flag:
            print(msg)
            break


def create_teacher():
    while 1:
        t_name = input('请输入要老师名字:>>').strip()
        if t_name == 'q':break
        res = school_interface.check_all_school()
        print(res)
        t_school = input('请输入学校:>>').strip()
        if t_school == 'q':break
        if t_school not in res:continue
        print(school_interface.add_teacher(t_name, t_school))
        flag, msg = teacher_interface.save_teacher(model.Teacher(t_name))
        if flag:
            print(msg)
            break


def create_course():
    while 1:
        c_name = input('请输入要创建课程名字:>>').strip()
        if c_name == 'q':break
        c_cycle = input('请输入课程的周期(月):>>').strip()
        if c_cycle == 'q':break
        c_money = input('请输入课程的金额:>>').strip()
        if c_money == 'q':break
        flag, msg = course_interface.save_course(model.Course(c_name, c_cycle, c_money))
        if flag:
            print(msg)
            break






