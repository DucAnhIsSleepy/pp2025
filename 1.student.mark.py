student_list = []
course_list = []

def add_student(name: str, id: str, DoB: str):
    s = {"Name": name,
         "ID": id,
         "Date of Birth": DoB}
    
    student_list.append(s)

def add_course(name: str, id: str):
    c = {"Name": name,
         "ID": id}
    
    course_list.append(c)
    
def display_student():
    for i in student_list:
        for l in i:
            print(f"{l}: {i[l]}")
        print()
            
def display_course():
    for i in course_list:
        for l in i:
            print(f"Course {l}: {i[l]}")

def add_score(sid: str, cid: str, mark):
    check = True
    for i in course_list:
        if i["ID"] == cid:
            check = False
            break
        
    if check:
        print("Course ID Not Found")
        return
    
    check = True
    for i in student_list:
        if i["ID"] == sid:
            i.update({f"Subject ID {cid} score":mark})
            return
        
    if check:
        print("Student ID Not Found")
        return

def main():
    add_student("Phạm Đức Anh","2410088","08/02/2006")
    add_student("Trần Khoa Nam","2410345","19/10/2006")
    add_course("Basic Programming","1")
    add_score("2410088","1",16.8)
    add_score("2410345","1",18)
    display_student()

if __name__ == "__main__":
    main()