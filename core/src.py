from core import admin, model, student, teacher


admin_dic = {
    '1': admin.create_school,
    '2': admin.create_teacher,
    '3': admin.create_course,
}


def admin():
    while 1:
        print("""
            1、创建学校
            2、创建老师
            3、创建课程
        """)
        choice = input('请输入要选择的序号:>>').strip()
        if choice == 'q':break
        if choice not in admin_dic:continue
        admin_dic[choice]()


student_dic = {
    '1': student.register,
    '2': student.login,
    '3': student.choice_school,
    '4': student.choice_course,
    '5': student.check_score
}


def student():
    while 1:
        print("""
            1、注册
            2、登陆
            3、选择学校
            4、选择课程
            5、查看成绩
        """)
        choice = input('请输入要选择的序号:>>').strip()
        if choice == 'q':break
        if choice not in student_dic:continue
        student_dic[choice]()


teacher_dic = {
    '0': teacher.login,
    '1': teacher.check_course,
    '2': teacher.choice_course,
    '3': teacher.check_course_student,
    '4': teacher.change_student_score,
}


def teacher():
    while 1:
        print("""
            0、登陆
            1、查看课程
            2、选择课程
            3、查看课程下的学生
            4、修改学生成绩
        """)
        choice = input('请输入要选择的序号:>>').strip()
        if choice == 'q':break
        if choice not in teacher_dic:continue
        teacher_dic[choice]()


dic = {
    '1': admin,
    '2': student,
    '3': teacher,
}


def run():
    while 1:
        print("""
            1、管理员
            2、学生
            3、教师
        """)
        choice = input('请输入要选择的序号:>>').strip()
        if choice == 'q':break
        if choice not in dic:continue
        dic[choice]()



