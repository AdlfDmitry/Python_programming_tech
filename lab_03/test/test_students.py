import unittest
from items.students import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Test Student", "123-456-7890", "test@example.com", "Male")
    
    def test_creation(self):
        self.assertEqual(str(self.student), "Name: Test Student, Phone: 123-456-7890, Email: test@example.com, Gender: Male")

    def test_eq(self):
        s2 = Student("Test Student", "123-456-7890", "test@example.com", "Male")
        s3 = Student("Other", "123", "test@example.com", "Male")
        self.assertEqual(self.student, s2)
        self.assertNotEqual(self.student, s3)
        self.assertNotEqual(self.student, "not a student")
    
    def test_lt(self):
        s1 = Student("Alice", "123", "test@example.com", "Male")
        s2 = Student("Bob", "123", "test@example.com", "Male")
        self.assertLess(s1, s2)