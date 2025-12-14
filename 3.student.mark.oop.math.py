import math
import numpy as np
import curses
from curses import wrapper

class thing:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        
    def display(self):
        print(f"Name: {self._name}")
        print(f"ID: {self._id}")
    
    #Getters   
    def get_name(self):
        return self._name
    
    def get_ID(self):
        return self._id
    
    #Setters
    def set_name(self, name: str):
        self._name = name
        
    def set_id(self, id: str):
        self._id = id
        
class student(thing):
    def __init__(self, name, id, DoB):
        super().__init__(name, id)
        self.__DoB = DoB
        self.__mark = {}
        self.__GPA = 0
        
    def display_info(self):
        print(f"Name: {self._name}")
        print(f"ID: {self._id}")
        print(f"Date of Birth: {self.__DoB}")
        print()

    def display_score(self):
        for k,v in self.__mark.items():
            print(f"Subject ID: {k}")
            print(f"Mark: {v}")
            print()
            
        print(f"GPA: {self.__GPA:.1f}")
        
    def update_GPA(self, course: 'course_list'):
        cal = []
        
        for c,m in self.__mark.items():
            for i in course.get_list():
                if c == i.get_ID():
                    cal += [m] * i.get_credit()
                    
        return np.average(cal)
        
    #Getters
    def get_DoB(self):
        return self.__DoB
    
    def get_GPA(self):
        return self.__GPA
    
    def get_mark(self):
        return self.__mark
    
    #Setters
    def set_DoB(self, DoB: str):
        self.__DoB = DoB
        
    def set_GPA(self, GPA: float):
        self.__GPA = GPA
        
    def set_mark(self, id: str, mark: float):
        self.__mark.update({id: mark})
        
class course(thing):
    def __init__(self, name, id, cred):
        super().__init__(name, id)
        self.__credit = cred
        
    def display(self):
        super().display()
        print(f"Credits: {self.__credit}")
        print()
        
    def get_credit(self):
        return self.__credit    
    
    def set_credit(self, cred):
        self.__credit = cred    
        
class list:
    def __init__(self):
        self._List = []
        
    def add(self):
        pass
    
    def display(self):
        pass
    
    def get_list(self):
        return self._List
    
class student_list(list):        
    def add(self, name : str, id : str, DoB : str):
        s = student(name, id, DoB)
        
        self._List.append(s)
        
    def display(self):
        for i in self._List:
            print(f"Student {self._List.index(i) + 1}:")
            print()
            i.display_info()
            i.display_score()
            
    def get_student(self, sid: str):
        for s in self._List:
            if s.get_ID() == sid:
                return s
        return None

class course_list(list):
    def add(self, name: str, id: str, cred: int):
        c = course(name, id, cred)
        
        self._List.append(c)

    def display(self):
        for i in self._List:
            print(f"Course {self._List.index(i) + 1}:")
            print()
            i.display()
            
    def get_course(self, cid: str):
        for c in self._List:
            if c.get_ID() == cid:
                return c
        return None

class mark_manage:
    def __init__(self, sl : student_list, cl : course_list):
        self.__student_list = sl
        self.__course_list = cl

    def add_score(self, mark: float, sid: str, cid: str):
        #This function add score of a specific student for a specific subject
        if self.__course_list.get_course(cid) is None:
            raise ValueError("Course ID not found")
        
        if not self.__student_list.get_student(sid) is None:
            s = self.__student_list.get_student(sid)
            #s.mark.update({cid: math.floor(mark*10)/10})
            s.set_mark(cid, math.floor(mark*10)/10)
            s.set_GPA(s.update_GPA(self.__course_list))
            
        else:
            raise ValueError("Student ID not found")

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