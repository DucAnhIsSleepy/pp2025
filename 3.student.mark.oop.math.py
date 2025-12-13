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
            if i.get_ID() == sid:
                return i
        return None
    
    def __find_course(self, cid):
        for i in self.course_list:
            if i.get_ID() == cid:
                return i
        return None

    def add_score(self, mark: float, sid: str, cid: str):
        #This function add score of a specific student for a specific subject
        if self.__find_course(cid) is None:
            raise ValueError("Course ID not found")
        
        if not self.__find_student(sid) is None:
            s = self.__find_student(sid)
            #s.mark.update({cid: math.floor(mark*10)/10})
            s.set_mark(cid, math.floor(mark*10)/10)
            s.GPA = s.set_GPA(self.__update_GPA(sid))
            
        else:
            raise ValueError("Student ID not found")

    def __update_GPA(self, sid):
        s = self.__find_student(sid)
        if s is None:
            raise ValueError("Student ID not found")
        
        cal = []
        
        for c,m in s.get_mark().items():
            for i in self.course_list:
                if c == i.get_ID():
                    cal += [m] * i.get_credit()
                    
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