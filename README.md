Course_Selection_System

    conf
        settings.py --> 关于文件中路径的配置文件
    
    core
        admin.py --> 管理员功能
        model.py --> 封装的一些类
        src.py --> 视图文件
        student.py --> 学生的一些相关功能
        teacher.py --> 老师的一些相关功能
    
    db
        course --> 管理员创建的课程存在这里面
            xxx.txt --> 是以pickle形式进行存储的
        school --> 管理员创建的学校放在这里面
            xxx.txt
        student --> 注册的学生信息放在这里面
            xxx.txt --> 是以pickle形式进行存储的
        teacher --> 管理员创建的老师信息放在这里面
            xxx.txt --> 是以pickle形式进行存储的
        db_handler.py --> 是interface中的文件调用其中的方法来操作文件数据的
    
    interface
        course_interface.py --> 课程接口
        school_interface.py --> 学校接口
        student_interface.py --> 学生接口
        teacher_interface.py --> 老师接口
    
    lib
        common.py --> 一些共用的方法(比如装饰器之类的...)
    
    start.py --> 根目录下的启动文件



