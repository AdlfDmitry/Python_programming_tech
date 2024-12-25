from sys import argv
from items.utils import FileUtils
from items.student_list import StudentList
from items.students import Student  

def main():
    if len(argv) < 2:
        print("Usage: python script.py <input_csv_file>")
        return

    input_file = argv[1]
    student_list = FileUtils.load_from_csv(input_file)  # Initialize student_list
    output_file = "output_csv_files_dir/"+input_file
    while True:
        action = input("Choose action [C: create, U: update, D: delete, P: print, X: exit]: ").lower()
        match action:
            case "c":
                name = input("Enter student name: ")
                phone = input("Enter student phone: ")
                email = input("Enter student email: ")
                gender = input("Enter student gender: ")
                new_student = Student(name, phone, email, gender)
                student_list.add_student(new_student)
                print("Student added successfully.")
            case "u":
                name = input("Enter name of the student to update: ")
                student = student_list.get_student(name)
                if not student:
                    print("Student not found.")
                    continue
                print(f"Current details - {student}")
                new_name = input(f"Enter new name (leave empty to keep '{student.name}'): ")
                new_phone = input(f"Enter new phone (leave empty to keep '{student.phone}'): ")
                new_email = input(f"Enter new email (leave empty to keep '{student.email}'): ")
                new_gender = input(f"Enter new gender (leave empty to keep '{student.gender}'): ")

                if student_list.update_student(name, new_name, new_phone, new_email, new_gender):
                  print("Student updated successfully.")
                else:
                  print("Student not found.")
            case "d":
                name = input("Enter name of the student to delete: ")
                student_list.delete_student(name)
                print(f"Deleted student with name {name}.")
            case "p":
                student_list.print_all()
            case "x":
                FileUtils.save_to_csv(output_file, student_list)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()