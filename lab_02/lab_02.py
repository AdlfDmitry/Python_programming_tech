import csv
from sys import argv

# Initial directory
student_list = []

def load_from_csv(file_name):
    """Load students from a CSV file into the student directory."""
    global student_list
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            student_list = list(reader)
        print("Data loaded successfully from", file_name)
    except FileNotFoundError:
        print("File not found. Starting with an empty directory.")

def save_to_csv(file_name):
    """Save the current student directory to a CSV file."""
    global student_list
    with open(file_name, mode='w', newline='') as file:
        if student_list:
            fieldnames = student_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_list)
        print("Data saved to", file_name)

def print_all():
    """Print all student records."""
    for student in student_list:
        print(
            f"Student name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Gender: {student['gender']}"
        )

def add_new_student():
    """Add a new student to the directory."""
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    gender = input("Enter student gender: ")
    new_student = {"name": name, "phone": phone, "email": email, "gender": gender}
    insert_position = next((i for i, student in enumerate(student_list) if name < student["name"]), len(student_list))
    student_list.insert(insert_position, new_student)
    print("Student added successfully.")

def delete_student():
    """Delete a student by name."""
    name = input("Enter name of the student to delete: ")
    global student_list
    student_list = [student for student in student_list if student["name"] != name]
    print(f"Deleted student with name {name}.")

def update_student():
    """Update a student's information."""
    name = input("Enter name of the student to update: ")
    student = next((s for s in student_list if s["name"] == name), None)
    if not student:
        print("Student not found.")
        return
    print(f"Current details - Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Gender: {student['gender']}")
    student["name"] = input(f"Enter new name (leave empty to keep '{student['name']}'): ") or student["name"]
    student["phone"] = input(f"Enter new phone (leave empty to keep '{student['phone']}'): ") or student["phone"]
    student["email"] = input(f"Enter new email (leave empty to keep '{student['email']}'): ") or student["email"]
    student["gender"] = input(f"Enter new gender (leave empty to keep '{student['gender']}'): ") or student["gender"]
    print("Student updated successfully.")

def main():
    """Main program loop."""
    if len(argv) < 2:
        print("Usage: python script.py <input_csv_file>")
        return

    input_file = argv[1]
   

    # Load data from CSV
    load_from_csv(input_file)

    while True:
        action = input("Choose action [C: create, U: update, D: delete, P: print, X: exit]: ").lower()
        match action:
            case "c":
                add_new_student()
            case "u":
                update_student()
            case "d":
                delete_student()
            case "p":
                print_all()
            case "x":
                save_to_csv(input_file)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()