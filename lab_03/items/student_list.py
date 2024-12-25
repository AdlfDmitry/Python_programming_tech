from items.students import Student

class StudentList:
    def __init__(self, students=None):
        self.students = students if students is not None else []

    def add_student(self, student):
        insert_position = next((i for i, s in enumerate(self.students) if student < s), len(self.students))
        self.students.insert(insert_position, student)

    def delete_student(self, name):
         self.students = [student for student in self.students if student.name != name]

    def update_student(self, name, new_name=None, new_phone=None, new_email=None, new_gender=None):
        for student in self.students:
            if student.name == name:
                student.name = new_name if new_name else student.name
                student.phone = new_phone if new_phone else student.phone
                student.email = new_email if new_email else student.email
                student.gender = new_gender if new_gender else student.gender
                return True
        return False

    def get_student(self, name):
        return next((student for student in self.students if student.name == name), None)

    def print_all(self):
        for student in self.students:
            print(student)
    
    def get_all_students(self):
        return self.students