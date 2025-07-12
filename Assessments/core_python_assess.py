# Core Python Assessment Test - Student Management System
def load_students():
    try:
        with open("student_data.txt", "r") as f:
            data = f.read()
            if data:
                return eval(data)  # Convert string back to dictionary
    except FileNotFoundError:
        pass
    return {}

def save_students(students):
    with open("student_data.txt", "w") as f:
        f.write(str(students))  # Convert dictionary to string and write to file

# Core Functions
def add_student(students):
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists. Try again.")
        return

    name = input("Enter Student Name: ")
    contact = input("Enter Contact Number (10 digits): ")

    if not contact.isdigit() or len(contact) != 10:
        print("Invalid contact number. Must be 10 digits.")
        return

    course = input("Enter Course Name: ")

    students[student_id] = {
        "name": name,
        "contact": contact,
        "course": course,
        "marks": {}
    }

    save_students(students)  # Save updated dictionary to file
    print("Student added and saved to file.\n")

def view_all_students(students):
    if not students:
        print("No students found.\n")
        return

    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Contact: {info['contact']}, Course: {info['course']}, Marks: {info['marks']}")
    print()

def view_specific_student(students):
    sid = input("Enter Student ID to view: ")
    if sid in students:
        print(students[sid])
    else:
        print("Student not found.\n")

def delete_student(students):
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        confirm = input("Are you sure you want to delete this student? (Y/N): ")
        if confirm.lower() == 'y':
            del students[sid]
            save_students(students)
            print("✅ Student deleted and file updated.\n")
        else:
            print("Deletion cancelled.\n")
    else:
        print("Student not found.\n")

def add_marks(students):
    sid = input("Enter Student ID to add marks: ")
    if sid not in students:
        print("Student not found.\n")
        return

    subject = input("Enter Subject Name: ")
    marks = input("Enter Marks: ")
    if not marks.isdigit():
        print("Invalid marks. Should be a number.")
        return

    students[sid]["marks"][subject] = int(marks)
    save_students(students)
    print("Marks added and file updated.\n")

# Main Menu
def main_menu():
    students = load_students()  # Load from file at start

    while True:
        print("\n====== Student Management System ======")
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
                add_student(students)
            elif choice == 2:
                delete_student(students)
            elif choice == 3:
                view_all_students(students)
            elif choice == 4:
                view_specific_student(students)
            else:
                print("Enter right choice.")
        
        elif role_id == 2:
            print("      1.Add Marks to Student\n"
                "      2.View All Student\n")
            fc = int(input("Enter a choice by faculty: "))
            if fc == 1:
                add_marks(students)
            elif fc == 2:
                view_all_students(students)
            else:
                print("Enter Valid Choice!")

# Run the program
main_menu()


    
