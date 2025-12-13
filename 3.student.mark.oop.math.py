import math
import numpy as np
import curses
from curses import wrapper

class thing:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        
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
        for k,v in self.mark.items():
            print(f"Subject ID: {k}")
            print(f"Mark: {v}")
            print()
            
        print(f"GPA: {self.GPA:.1f}")
        
class course(thing):
    def __init__(self, name, id, cred):
        super().__init__(name, id)
        self.credit = cred
        
    def display(self):
        super().display()
        print(f"Credits: {self.credit}")
        print()
        
class list:
    def __init__(self):
        self.List = []
        
    def add(self):
        pass
    
    def display(self):
        pass
    
class student_list(list):        
    def add(self, name : str, id : str, DoB : str):
        s = student(name, id, DoB)
        
        self.List.append(s)
        
    def display(self):
        for i in self.List:
            print(f"Student {self.List.index(i) + 1}:")
            print()
            i.display_info()
            i.display_score()

class course_list(list):
    def add(self, name: str, id: str, cred: int):
        c = course(name, id, cred)
        
        self.List.append(c)

    def display(self):
        for i in self.List:
            print(f"Course {self.List.index(i) + 1}:")
            print()
            i.display()

class mark_manage:
    def __init__(self, sl : object, cl : object):
        self.student_list = sl.List
        self.course_list = cl.List

    def __find_student(self, sid):
        for i in self.student_list:
            if i.id == sid:
                return i
        return None
    
    def __find_course(self, cid):
        for i in self.course_list:
            if i.id == cid:
                return i
        return None

    def add_score(self, mark: float, sid: str, cid: str):
        #This function add score of a specific student for a specific subject
        if self.__find_course(cid) is None:
            raise ValueError("Course ID not found")
        
        if not self.__find_student(sid) is None:
            s = self.__find_student(sid)
            s.mark.update({cid: math.floor(mark*10)/10})
            s.GPA = self.__update_GPA(sid)
            
        else:
            raise ValueError("Student ID not found")

    def __update_GPA(self, sid):
        s = self.__find_student(sid)
        if s is None:
            raise ValueError("Student ID not found")
        
        cal = []
        
        for c,m in s.mark.items():
            for i in self.course_list:
                if c == i.id:
                    cal += [m] * i.credit
                    
        store = np.array(cal)
        return np.average(store)
                    
def main():
    testc = course_list()
    testc.add("Basic Programming","1",3)
    testc.add("Advanced Programming","2",4)
    
    tests = student_list()
    tests.add("Phạm Đức Anh","2410088","08/02/2006")
    
    testm = mark_manage(tests, testc)
    testm.add_score(16.8888, "2410088", "1")
    testm.add_score(17.6666, "2410088", "2")
    tests.display()

if __name__ == "__main__":
    main()