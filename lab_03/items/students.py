class Student:
    def __init__(self, name, phone, email, gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Gender: {self.gender}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.name == other.name and
                    self.phone == other.phone and
                    self.email == other.email and
                    self.gender == other.gender)
        return False
    
    def __lt__(self, other):
      return self.name < other.name