from student import Student
from student_list import StudentList
import sys
Csv_file = "students.csv"
def main():

    student_list = StudentList()
    file_name = sys.argv[1] if len(sys.argv) > 1 else Csv_file

    print(f"Using file: {file_name}")
    student_list.import_students(file_name)

    while True:
        UserInput = input("\nChoose action [C - Create, U - Update, D - Delete, P - Print, S - Save, E - Exit]: ").strip().upper()
        
        if UserInput == "C":
            print("Add New Student")
            name = input("Enter student name: ").strip()
            phone = input("Enter student phone: ").strip()
            email = input("Enter student email: ").strip()
            age = input("Enter student age: ").strip()
            student = Student(name=name, phone=phone, email=email, age=age)
            student_list.add_student(student)
            print("Student added")
        
        elif UserInput == "U":
            print(" Update Student Information")
            name = input("Enter the name of the student to update: ").strip()
            student = student_list.find_student(name)
            if student:
                print(f"Found student: {student}")
                new_name = input("Enter new name (press Enter to keep): ").strip()
                new_phone = input("Enter new phone (press Enter to keep): ").strip()
                new_email = input("Enter new email (press Enter to keep): ").strip()
                new_age = input("Enter new age (press Enter to keep): ").strip()
                success = student_list.update_student(name, new_name=new_name, new_phone=new_phone, new_email=new_email, new_age=new_age)
                if success:
                    print("Student updated")
                else:
                    print("Failed to update")
            else:
                print("Student not found.")
        
        elif UserInput == "D":
            print("Delete Student")
            name = input("Enter the name of the student to delete: ").strip()
            success = student_list.delete_student(name)
            if success:
                print("Student deleted")
            else:
                print("Student not found.")
        
        elif UserInput == "P":
            print("List of Students:")
            student_list.print_all_students()
        
        elif UserInput == "S":
            student_list.save_students(file_name)
            print("Students saved successfully.")
        
        elif UserInput == "E":
            student_list.save_students(file_name)
            print("Exiting program")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()