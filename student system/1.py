import time
import os
def menu():
    print('''
            ====================Student Information System===================

            ===========================Function Menue========================

            1.insert
            
            2.search
            
            3.delete
            
            4.modify
            
            5.sort
            
            6.total student number
            
            7.show
            
            0.exit
            =================================================================
          '''
          )

def save(student):
    try:
        students_txt=open("1.txt","a")
    except Exception as e:
        students_txt = open("1.txt","w")
    for info in student:
        students_txt.write(str(info)+"\n")
    students_txt.close()
        
def insert():
    studentlist=[]
    mark=True
    while mark:
        id=input("Please enter the ID number(like 1001):")
        if not id:
            break
        name=input("Please enter the student's name:")
        if not name:
            break
        try:
            en_result=int(input("Please enter the english grade:"))
            py_result=int(input("please enter the python grade:"))
            c_result=int(input("Please enter the c grade:"))
        except:
            print("invalid input, it's not integer, please enter again!")
            continue
        student={"id":id,"name":name,"english":en_result,"python":py_result,"c":c_result}
        studentlist.append(student)
        inputmark=input("if you want to continue?(y/n):")
        if inputmark!="y":
            mark=False
    save(studentlist)
    print("insert finished")


def show_student(studentList):
    if not studentList:
        print("(o@.@o) There is no student information!(o@.@o) \n")
        return
    format_title="{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID","Name","English","Python","C","total"))
    format_data="{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"),
            info.get("name"),str(info.get("english")),str(info.get("python")),
            str(info.get("c")),str(info.get("english")+info.get("python")+info.get("c")).center(12)))

def search():
    mark=True
    student_query=[]
    while mark==True:
        id=""
        name=""
        if os.path.exists("1.txt"):
            mode=input("which mode you want to choose? (1:ID number 2:Name)")
            if mode=="1":
                id=input("Please enter the ID number:")
            elif mode=="2":
                name=input("Please enter the name:")
            else:
                print("The mode is not valid, please input again!")
                search()
            with open ("1.txt","r") as file:
                student=file.readlines()
                for list in student:
                    d=dict(eval(list))
                    if id !="":
                        if id==d["id"]:
                            student_query.append(d)
                    elif name!="":
                        if name==d["name"]:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputmark=input("Do you want to continue?(y/n)")
                if inputmark=="n":
                    break
        else:
            print("There is no student information!")
            return

def delete():
    mark=True
    while mark:
        studentID= input("Please enter the student ID number:")
        if studentID != "":
            if os.path.exists("1.txt"):
                with open ("1.txt","r") as rfile:
                    student_old=rfile.readlines()
            else:
                student_old=[]
            ifdel=False
            if student_old:
                with open("1.txt","w") as wfile:
                    d={}
                    for list in student_old:
                        d=dict(eval(list))
                        if d["id"] !=studentID:
                            wfile.write(str(d)+"\n")
                        else:
                            ifdel=True
                    if ifdel:
                        print("The student information has been deleted!")
                    else:
                        print("We can't find the student, sorry")
            else:
                print("There is no student!")
                break
            show()
            inputMark=input("if you want to continue?(y/n):")
            if inputMark=="y":
                mark=True
            else:
                mark=False

def modify():
    show()
    if os.path.exists("1.txt"):
        with open("1.txt","r") as rfile:
            student_old=rfile.readlines()
    else:
        return
    studentid=input("Please enter the student id number:")
    with open("1.txt","w") as wfile:
        for student in student_old:
            d=dict(eval(student))
            if d["id"]==studentid:
                print("We have found this student and can modify his information!")
                while True:
                    try:
                        d["name"]=input("Please enter the name:")
                        d["english"]=int(input("please enter the english result:"))
                        d["python"]=int(input("please enter the python result:"))
                        d["c"]=int(input("please enter the c result:"))
                    except:
                        print("valid input, please try it again!")
                    else:
                        break
                student = str(d)
                wfile.write(student+"\n")
                print("modified successfully!")
            else:
                print("No student ID number is {}".format(studentid))
                wfile.write(student)
    mark = input("Do you want to continue?(y/n)")
    if mark == "y":
        modify()

def sort():
    return

def total():
    if os.path.exists("1.txt"):
        with open("1.txt","r") as rfile:
            student_old=rfile.readlines()
            if student_old:
                print("There are {} students".format(len(student_old)))
            else:
                print("You haven't recorded any student's information!")
    else:
        print("You haven't recorded any student's information!")
        
def show():
    student_new=[]
    if os.path.exists("1.txt"):
        with open("1.txt","r") as rfile:
            student_old=rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("There is no information saved")

def main():
    ctrl=True
    while(ctrl):
        menu()
        option=int(input("Please enter the number:"))
        options=[0,1,2,3,4,5,6,7]
        if option in options:
            if option==0:
                print("You have quited the system, goodbye!")
                time.sleep(5)
                ctrl=False
            elif option==1:
                insert()
            elif option==2:
                search()
            elif option==3:
                delete()
            elif option==4:
                modify()
            elif option==5:
                sort()
            elif option==6:
                total()
            elif option==7:
                show()
        else:
            option=int(input("Please enter a valid number again:"))
            
main()
