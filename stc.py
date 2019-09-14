from dataclasses import dataclass, field
from typing import List, Set
import random


@dataclass
class Teacher:
    """
    教师类
    """
    id: int
    name: str
    phone_number: str


@dataclass
class Course:
    """
    课程类
    """
    id: int
    name: str
    teacher: object = field(default_factory=Teacher)

    def add_tea(self, tea_name) -> str:
        """
        给课程添加一个教师
        """
        self._teacher = tea_name

    def check_all_info(self):
        """
        查看课程信息
        """
        print("{}课程的编号、教师分别是:{}、{}".format(self.name, self.id, self.teacher))


@dataclass
class Student:
    """
    学生类
    """
    id: int
    name: str
    address: str
    courses: List = field(default_factory=list)

    def add_course(self, course) -> Course:
        """
        添加课程
        课程信息包括:
            课程编号
            课程名称
            授课教师
        """
        self._courses.append(course)

    def check_courses(self):
        """
        查看该学生所有课程
        """
        print("{}选的课程有:{}".format(self.name, self._courses))


if __name__ == "__main__":
    """
    请完成以上三个类.创建6个课程，6个教师.给课程安排好教师.然后创建30个学生.
    每个学生随机被分配3个课程.最终显示出这三十个学生的选课情况以及任课教师的电话

    先解析上面的要求：
        三个类，学生包含课程，课程中包含教师
        所以需要先构建6个教师
    """
    tea_6 = []
    for i in range(1, 7):
        teacher = Teacher(
            i,
            "张{}".format(str(i)),
            "1873232323{}".format(str(i))
        )
        tea_6.append(teacher)
    print(tea_6, end="\n")  # 打印6个教师信息

    cou_6 = []
    cou_name = ["语文", "数学", "英语", "化学", "物理", "生物"]
    for index, tea in enumerate(tea_6):
        course = Course(
            index,
            cou_name[index],
            tea
        )
        cou_6.append(course)
    print(cou_6, end="\n")  # 　打印6个课程信息

    # stu_30 = [] #
    for i in range(1, 31):  # 创建30个学生
        # 注意一个学生需要三门随机课程,使用random
        course_3 = random.sample(cou_6, 3)  # 随机出三门课程
        student = Student(
            id=i,
            name="学生{}".format(str(i)),
            address="小区{}".format(str(i)),
            courses=course_3
        )

        # stu_30.append(student)

        # 最后直接打印这三十个学生的选课情况以及任课教师的电话
        print("{}的所选三门课程分别为:{}".format(
                student.name,
                ["课程:{},编号:{},教师:{},电话:{}".format(
                    cou.name,
                    cou.id,
                    cou.teacher.name,
                    cou.teacher.phone_number
                ) for cou in student.courses]
            )
        )
