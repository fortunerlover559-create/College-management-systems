import json
import os

def Admin_login_check()l:
    with open("password.json","r") as f:
        data =json.load(f) 
    
    if (username == data["Admin"][0]) and (password == data["Admin"][1]):
        print("login successfully as Admin")
    else:
        os.system('cls')
        print("Invalid username/password ")  
        exit()


def Teacher_login_check():
    with open("password.json","r") as f:
        data =json.load(f) 
    name = input("Enter your name: ")
    if (username == data[f"{name}"][0]) and (password == data[f"{name}"][1]):
        print("login successfully as Teacher")
    else:
        os.system('cls')
        print("Invalid username/password ")
        exit()


def feature(a):
    print(30*"=")
    for i,a in enumerate(a , start=1):
        print(f" {i}).{a}") 
    print(30*"=")    




def load():
    with open ("Teacher_Record.json","r") as f:
        data = json.load(f)
        return data 



def save(data):
    with open("Teacher_Record.json","w") as f:
        json.dump(data,f,indent=4)    




def Add_Teacher_Record():
    data = load()
    os.system("cls")
    name = input("Enter your name: ")
    phon_number = int(input("enter your phone number: "))
    Age = int(input("Enter your age: "))
    class_name = input("Enter your class name: ")
    subject_name = input("Enter your subject name: ")

    data["teacher"].append({
        "name":name,
        "phon number":phon_number,
        "Age":Age,
        "Class":class_name,
        "subject name":subject_name
    })

    save(data)
    print("The teacher data has been added successfully...")




 

def Add_Student_Record():
    data = load()
    os.system("cls")
    name = input("Enter your name: ")
    roll_number =int(input("Enter your Roll number: ")) 
    Age = int(input("Enter your age: "))
    class_name = input("Enter your class name: ")
    subject_name = input("Enter your subject name: ")
    marks = int(input("Enter your marks: "))
    CGPA = int(input("Enter your CGPA: "))
    adress = input("Enter your Adress: ")

    data["student"].append({
        "name":name,
        "roll number":roll_number,
        "Age":Age,
        "Class":class_name,
        "subject name":subject_name,
        "marks":marks,
        "CGPA":CGPA,
        "Adress" : adress

    })

    save(data)
    print("The student data has been added successfully... ")






def view_Teacher_Record():
    data = load()
    os.system('cls')
    print("----Teacher_Record------------")
    for t in data["teacher"]:
        print(t)
    print(30*"=")    


    
  


def view_Student_Record():
    data = load()
    os.system("cls")
    print("="*30)
    print("------Student_Record------------")
    print("="*30)
    for s in data["student"]:
        print(s)
        
    print(30*"=")    






def Admin_work():
    if (admin_choice ==1):
        Add_Teacher_Record()
    elif(admin_choice ==2):
        view_Teacher_Record()   
    elif(admin_choice == 3):
        search_teacher()
    elif(admin_choice == 4):
        delete_teacher()
    elif(admin_choice == 5):
        Add_Student_Record()
    elif(admin_choice == 6):
        view_Student_Record()  
    elif(admin_choice == 7):
        update_student_record()
    elif(admin_choice == 8):
        search_student()  
    elif(admin_choice == 9):
        delete_student() 
    elif(admin_choice == 10):
        student_average()    
    else:
        os.system('cls')
        print("Thanks for using A.H college managment system ")




def Teacher_work():
    if (teacher_choice == 1):
        Add_Student_Record()
    elif (teacher_choice == 2):
        view_Student_Record() 
    elif(teacher_choice == 3):
        update_student_record()
    elif(teacher_choice == 4):
        search_student() 
    elif(teacher_choice == 5):
        delete_student()
    elif(teacher_choice == 6):
        student_average()
                   
    else:    
        print("Thanks for using A.H college managment system ")




update_menu = [
    "Name", "Age", "Class", "Subject",
    "Marks", "CGPA", "Address"
]

def update_work(student, choice):
    if choice == 1:
        student["name"] = input("Enter new name: ")
    elif choice == 2:
        student["Age"] = int(input("Enter new age: "))
    elif choice == 3:
        student["Class"] = input("Enter new class: ")
    elif choice == 4:
        student["subject name"] = input("Enter new subject: ")
    elif choice == 5:
        student["marks"] = int(input("Enter new marks: "))
    elif choice == 6:
        student["CGPA"] = int(input("Enter new CGPA: "))
    elif choice == 7:
        student["Address"] = input("Enter new address: ")
    else:
        print("Invalid choice")


def update_student_record():
    data = load()
    os.system("cls")

    feature(update_menu)

    choice = int(input("What do you want to update: "))
    roll = int(input("Enter roll number: "))

    for student in data["student"]:
        if student["roll number"] == roll:
            update_work(student, choice)
            save(data)
            print("The student Record has been updated successfully...")
            return

    print("Student record not found...")




def search_student():
    data = load()
    os.system("cls")

    roll = int(input("Enter roll number: "))

    for s in data["student"]:
        if s["roll number"] == roll:
            print("="*10)
            print("Student Found:", s)
            return
    print("Student not found")




def search_teacher():
    data = load()
    os.system("cls")

    name = input("Enter teacher name: ").lower()

    for t in data["teacher"]:
        if t["name"].lower() == name:
            print("Teacher Found:", t)
            return
    print("Teacher not found")



def delete_student():
    data = load()
    os.system("cls")

    roll = int(input("Enter roll number: "))

    for s in data["student"]:
        if s["roll number"] == roll:
            data["student"].remove(s)
            save(data)
            print("Student deleted")
            return
    print("Student not found")



def delete_teacher():
    data = load()
    os.system("cls")

    name = input("Enter teacher name: ").lower()

    for t in data["teacher"]:
        if t["name"].lower() == name:
            data["teacher"].remove(t)
            save(data)
            print("Teacher deleted")
            return
    print("Teacher not found")



def student_average():
    data = load()
    os.system("cls")

    if not data["student"]:
        print("No students found")
        return

    total = sum(s["marks"] for s in data["student"])
    avg = total / len(data["student"])
    print("Average Marks of All Students:", round(avg, 2))


#---------------------- MAIN CODE OF THIS PROJECT ----------------------------------------------------


print(50*"*")
print("Welcome to A.H College Menagment System ")

print(50*"*")

choice = input("login as admin/teacher: ").lower()
if (choice == "admin" or choice == "teacher"):
    pass
    username = input("enter your username: ").lower()
    password = int(input("enter your password: "))
else:
    print("=" * 30)
    print("Invalid input run code again ")
    print("=" * 30)  
    exit()  

os.system('cls')

print(30*"=")
Admin_display = ["Add Teacher Record","View Teacher Record","Search Teacher data","Delete Teacher Data","Add Student Record","View Student Record","Update student record","Search student data","Delete Student Data","Average of marks","Exit"]
Teacher_display = ["Add Student Record","View Student Record","Update student record","Search student data","Delete Student Data","Average of marks","Exit"] 

if choice == "admin":
    Admin_login_check()
     
    while True:
        feature(Admin_display)
        admin_choice = int(input("What do you want to do? "))
        print(30*"=") 
        os.system('cls')
        Admin_work()
        if admin_choice == 11:
            exit()

elif choice == "teacher":
    Teacher_login_check() 
    while True:
        feature(Teacher_display)
        teacher_choice = int(input("Enter number what you want "))
        print(30*"=")  
        os.system('cls')
        Teacher_work()
        print(30*"=")
        if teacher_choice == 7:
            exit()          
                    

       
        






