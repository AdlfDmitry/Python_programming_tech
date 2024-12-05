import csv
import sys
students = []

#Loading data
def load_from_csv(filename):
    global students
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]
        print(f"Data was loaded succesfuly {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Loading data error: {e}")

#Saving data
def save_to_csv(filename):
    try:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ["name", "phone", "email", "gender"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Data saved succesfuly {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

#Data Print
def print_all_students():
    if not students:
        print("Student list is empty")
        return
    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Gender: {student['gender']}")

#Add new data    
def add_new_student():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    gender = input("Enter student gender: ")
    new_student = {"name": name, "phone": phone, "email": email, "gender": gender}
    students.append(new_student)
    students.sort(key=lambda x: x['name'])
    print("New student added succesfuly")   

#Delete data
def delete_student():
    name = input("Enter the name of the student to delete: ")
    global students
    filtered_students = [student for student in students if student['name'] != name]
    if len(filtered_students) < len(students):
        students = filtered_students
        print(f"Student {name} deleted")
    else:
        print(f"Student {name} not found")
#Update data
def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student['name'] == name:
            print(f"Curent data: {student}")
            student['name'] = input(f"New name (current: {student['name']}): ") or student['name']
            student['phone'] = input(f"New phone (current: {student['phone']}): ") or student['phone']
            student['email'] = input(f"New email (current: {student['email']}): ") or student['email']
            student['gender'] = input(f"New gender (current: {student['gender']}): ") or student['gender']
            print(f"Student {name} data changed succesfuly")
            return
    print(f"Student {name} not found")
    
#Get file name from user 
def get_filename_from_user():
    filename = input("Enter CSV file name: ").strip()
    return filename           
def main():
    if len(sys.argv) > 1:
        load_from_csv(sys.argv[1])

    while True:
        choice = input("Choose action: [C]reate, [U]pdate, [D]elete, [P]rint, E[x]it: ").strip().lower()
        match choice:
            case "c":
                add_new_student()
            case "u":
                update_student()
            case "d":
                delete_student()
            case "p":
                print_all_students()
            case "x":
                save_to_csv("students.csv")
                print("Exiting")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()