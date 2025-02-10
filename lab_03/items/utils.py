import csv
import sys
from items.student_list import student_list

class CSV_operations:
    def __init__(self, studn_list:student_list):
        self.studn_list = studn_list
        self.file = sys.argv[1]
    
    def loadCSV(self):
        self.studn_list.student_list = []
        try:
            with open(self.file, "r", newline ='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.studn_list.addNewElement(row)
                print(f"Data loaded succesfully")
        except FileNotFoundError:
            print(f"No file named csvfile - {self.file}, it will be created, when you exit")

    def saveCSV(self):
        with open(self.file, "w", newline ='') as csvfile:
            fieldnames = ['name', 'phone', 'email', 'gender']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.studn_list.student_list:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "email": student.email,
                    "gender": student.gender
                })
            print(f"Data in file was updated ")