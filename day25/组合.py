#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

# 一个类由不同的类组合而来，这样做的目的是使类之间产生联系

class School:
    """School"""
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

    def recruit_students(self):
        """recruit"""
        print('%s is recruiting student in %s ' % (self.name,self.addr))
        # return '%s is recruiting student in %s ' % (self.name,self.addr)

class Teacher:
    """Teacher"""
    def __init__(self,name,school,course):
        self.name = name
        self.school = school
        self.course = course

    def teaching(self):
        """teaching"""
        print('%s is teaching %s in %s' % (self.name,self.course.name,self.school.name))
        # return '% is teaching %s in %s' % (self.name,self.course.name,self.school.name)

class Course:
    """Course"""
    def __init__(self,name,school):
        self.name = name
        self.school = school

    def course(self):
        """course"""
        print('%s belong to %s' % (self.name,self.school.name))
        # return '%s belong to %s' % (self.name,self.school.name)

s = School('oldboy','beijing')
c = Course('python',s)
t = Teacher('alex',s,c)

s.recruit_students()
c.course()
t.teaching()
