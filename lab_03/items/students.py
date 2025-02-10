class Student:
    def __init__(self,name,phone,email,gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
    def __str__(self):
        return f"Name: '{self.name}', phone: '{self.phone}', email: '{self.email}', gender: '{self.gender}' "