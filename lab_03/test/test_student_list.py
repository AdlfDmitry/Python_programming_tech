import unittest
from items.students import Student
from items.student_list import StudentList

class TestStudentList(unittest.TestCase): #hetitage
    def setUp(self):
        self.s1 = Student("Alice", "1", "a@ex.com", "F")
        self.s2 = Student("Bob", "2", "b@ex.com", "M")
        self.list = StudentList()

    def test_add_delete(self):
        self.list.add_student(self.s1)
        self.assertIn(self.s1, self.list.students)
        self.list.add_student(self.s2)
        self.list.delete_student("Bob")
        self.assertEqual(len(self.list.students), 0)

    def test_update(self):
        self.list.add_student(self.s1)
        self.list.update_student("Alice", new_phone="111")
        self.assertEqual(self.list.students[0].phone, "111")
        self.list.update_student("Alice",new_email="new@ex.com",new_name="Alisa",new_gender="O")
        self.assertEqual(self.list.students[0].email,"new@ex.com")
        self.assertEqual(self.list.students[0].name, "Alisa")
        self.assertEqual(self.list.students[0].gender,"O")
        self.assertFalse(self.list.update_student("NonExistent", "New Name"))
    
    def test_get_student(self):
        self.list.add_student(self.s1)
        self.assertEqual(self.list.get_student("Alice"), self.s1)
        self.assertIsNone(self.list.get_student("NonExistent"))
    
    def test_get_all(self):
        self.list.add_student(self.s1)
        self.list.add_student(self.s2)
        self.assertEqual(self.list.get_all_students(), [self.s1, self.s2])