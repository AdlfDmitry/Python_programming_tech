import csv
from items.students import Student
from items.student_list import StudentList

class FileUtils:
    @staticmethod
    def load_from_csv(file_name):
        try:
            students = []
            with open(file_name, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row['name'], row['phone'], row['email'], row['gender'])
                    students.append(student)
            return StudentList(students)
        except FileNotFoundError:
            print("File not found. Starting with an empty directory.")
            return StudentList()
    
    @staticmethod
    def save_to_csv(file_name, student_list):
        with open(file_name, mode='w', newline='') as file:
            if student_list.students:
                fieldnames = ["name", "phone", "email", "gender"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows([student.__dict__ for student in student_list.students])
            print("Data saved to", file_name)