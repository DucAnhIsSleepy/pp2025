import math
import numpy as np

class thing:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    @property
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print()
        
class student(thing):
    def __init__(self, name, id, DoB):
        super().__init__(name, id)
        self.DoB = DoB
        self.mark = {}
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Date of Birth: {self.DoB}")
        print()

    def display_score(self):
        for i in self.mark:
            print(f"Subject ID: {i}")
            print(f"Mark: {self.mark[i]}")
        
class course(thing):
    def __init__(self, name, id):
        super().__init__(name, id)
        
class list:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, name, id ,DoB):
        s = student(name, id, DoB)
        self.student_list.append(s)

    def display_student(self):
        for i in self.student_list:
            i.display_info()
            i.display_score()

    def add_course(self, name, id):
        c = course(name, id)
        self.course_list.append(c)
    
    def display_course(self):
        for i in self.course_list:
            i.display
    
    def add_score(self, sid: str, cid: str, mark: float):
        check = True
        #check if course ID available
        for c in self.course_list:
            if c.id == cid:
                check = False
                break
        
        if check:
            print("Course ID not found")
            return
        
        check = True
        #check if student ID available and add mark
        for s in self.student_list:
            if s.id == sid:
                check = False
                s.mark[cid] = math.floor(mark*10)/10
                return
            
        if check:
            print("Student ID not found")
            return
        
def main():
    test = list()
    test.add_course("Basic Programming","1")
    test.add_course("Advanced Programming","2")
    test.add_student("Phạm Đức Anh","2410088","08/02/2006")
    test.add_score("2410088","1",16.8888)
    test.display_student()

main()