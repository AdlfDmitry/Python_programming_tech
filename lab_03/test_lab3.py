import unittest
from student import Student
from student_list import StudentList
import os
import csv

class TestStudentList(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()
        self.test_file = "test_students.csv"

    def test_add_student(self):
        student = Student(name="Alpha", phone="111111111", email="alpha@gmail", age = 19)
        self.student_list.add_student(student)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "Alpha")

    def test_delete_student(self):
        student = Student(name="Alpha", phone="111111111", email ="alpha@gmail", age = 19)
        self.student_list.add_student(student)
        self.student_list.delete_student("Alpha")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        student = Student(name="Alpha", phone="111111111",email="alpha@gmail", age = 19)
        self.student_list.add_student(student)
        self.student_list.update_student("Alpha", new_name="Bravo", new_phone="22222222", new_email="bravo@gmail", new_age= 20)
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.name, "Bravo")
        self.assertEqual(updated_student.phone, "22222222")
        self.assertEqual(updated_student.email, "bravo@gmail")
        self.assertEqual(updated_student.age, 20)

    def test_save_students(self):
        student1 = Student(name="Alpha", phone="111111111", email="alpha@gmail", age= 19)
        student2 = Student(name="Bravo", phone="22222222", email="bravo@gmail", age = 20)
        self.student_list.add_student(student1)
        self.student_list.add_student(student2)

        self.student_list.save_students(self.test_file)

        with open(self.test_file, "r", encoding="utf-8") as file:
            content = file.readlines()
        self.assertEqual(len(content), 3)  
        self.assertIn("Alpha,111111111,alpha@gmail,19\n", content[1:])
        self.assertIn("Bravo,22222222,bravo@gmail,20\n", content[1:])

if __name__ == "__main__":
    unittest.main()