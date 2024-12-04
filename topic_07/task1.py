class Student:
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"
students = [
    Student("Dmitry", 20),
    Student("Alex", 22),
    Student("Olena", 19),
    Student("Ivan", 21)
]
while True:
    print("Choose sorting key: 1 for age, 2 for name")
    choice = input("Your choice: ")
    if choice == "1":
        sorted_students = sorted(students, key=lambda student: student.age)
    elif choice == "2":
        sorted_students = sorted(students, key=lambda student: student.name)
    else:
        print("Wrong choice")
        continue
    for student in sorted_students:
        print(student)

