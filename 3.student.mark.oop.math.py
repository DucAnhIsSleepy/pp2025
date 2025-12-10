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
        self.GPA = 0
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Date of Birth: {self.DoB}")
        print()

    def display_score(self):
        for i in self.mark:
            print(f"Subject ID: {i}")
            print(f"Mark: {self.mark[i]}")
            print()
            
        print(f"GPA: {self.GPA:.1f}")            
class course(thing):
    def __init__(self, name, id, cred):
        super().__init__(name, id)
        self.credit = cred
        
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

    def add_course(self, name, id, cred):
        c = course(name, id, cred)
        self.course_list.append(c)
    
    def display_course(self):
        for i in self.course_list:
            i.display
    
    def add_score(self, sid: str, cid: str, mark: float):
        check = True
        current_student = None
        
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
                current_student = s
                current_student.mark[cid] = math.floor(mark*10)/10
                return
            
        if check:
            print("Student ID not found")
            return
        
        #update GPA
        

def main():
    test = list()
    test.add_course("Basic Programming","1",3)
    test.add_course("Advanced Programming","2",4)
    test.add_student("Phạm Đức Anh","2410088","08/02/2006")
    test.add_score("2410088","1",16.8888)
    test.add_score("2410088","2",17.6666)
    test.display_student()

if __name__ == "__main__":
    main()