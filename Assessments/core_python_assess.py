# Core Python Assessment Test - Student Management System

studt = {}

class student_detail:
          
    def add_student(self):
        stud = open("Student.txt","a")
        no = int
        fn=str
        ln=str
        cn=int
        self.no=input("Enter serial number: ")
        while True:
            self.fn = input("Enter First Name: ").upper()
            self.ln = input("Enter Last Name: ").upper()
            if not self.fn.isalpha() and not self.ln.isalpha():
                print("Name should contain only letters.")
            else:
                break
        while True:
            self.cn = input("Enter contact number: ")
            if len(self.cn) != 10 : 
                print("Number should consider only digits and it should only be 10. ")
            else:
                break
        self.ask = int(input("How many Entry you want to make for subjects and marks? "))
        for i in range(self.ask):
            self.sub = input("Enter Subject: ")
            self.marks = int(input("Enter Marks: "))
            self.fee = int(input("Enter Fees: "))
        studt[no]={
            "First Name":self.fn,
            "Last Name":self.ln,
            "Contact Number":self.cn,
            "Subject":{},
            "Marks":{},
            "Fee":{}        
        }
        with open("Student.txt","w") as f:
            f.write("Students:",{studt})
        f.write("==========================================\n")

    def remove_student():
        pass

    def view_all_stud():
        pass

    def view_specific_student():
        pass

sd = student_detail()

while True:
    #MENU
    print("      Press 1 for Counsellor\n"
          "      Press 2 for Faculty\n"
          "      Press 3 for Student\n")

    role_id = int(input("Enter the role ID: "))

    if role_id == 1:
        print("      1. Add Student\n"
            "      2. Remove Student\n"
            "      3. View All Student\n"
            "      4. View Specific Student\n")
        choice = int(input("Enter a choice by counsellor: "))
        if choice == 1:
            sd.add_student()
        elif choice == 2:
            sd.remove_student()
        elif choice == 3:
            sd.view_all_stud()
        elif choice == 4:
            sd.view_specific_student()
        else:
            print("Enter right choice.")

    elif role_id == 2:
        print("      1.Add Marks to Student\n"
              "      2.View All Student\n")
        fc = int(input("Enter a choice by faculty: "))
        if fc == 1:
            sd.add_student()
        elif fc == 2:
            sd.view_all_stud()
        else:
            print("Enter Valid Choice!")


    
