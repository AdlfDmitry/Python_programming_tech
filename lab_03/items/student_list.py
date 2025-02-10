from items.students import Student

class student_list:

    def __init__(self):

        self.student_list=[]

    def prinList(self):
        for student in self.student_list:
            print(student)
    
    def addingNew(self):
        name = input("Pease enter student name: ")
        phone = input("Enter student phone: ")
        email = input("Enter student email: ")
        gender = input("Enter student gender: ")
        newItem = {"name": name, "phone": phone, "email": email, "gender": gender}
        return newItem

    def addNewElement(self,newItem):
        student = Student(newItem["name"], newItem["phone"], newItem["email"], newItem["gender"])

        insertPosition = 0
        for item in self.student_list:
            if newItem["name"] > item.name:
                insertPosition += 1
            else:
                break
        self.student_list.insert(insertPosition, student)
        return

    def deleteElement(self,name):
        deletePosition = -1
        for item in self.student_list:
            if name == item.name:
                deletePosition = self.student_list.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.student_list[deletePosition]
        return

    def updatingData(self, Prev_Stud):
        updated_name = input("Pease enter new student name or skip: ") or Prev_Stud.name
        updated_phone = input("Enter new student phone or skip: ") or Prev_Stud.phone
        updated_mail = input("Enter new student email or skip: ") or Prev_Stud.email
        updated_gender = input("Enter new student gender or skip: ") or Prev_Stud.gender    
        updated_item = {"name": updated_name, "phone": updated_phone, "email": updated_mail, "gender": updated_gender}
        return updated_item

    def updateElement(self,name):
        searchPosition = -1
        for item in self.student_list:
            if name == item.name:
                searchPosition = self.student_list.index(item)
                break
        if searchPosition == -1:
            print("Element was not found")
        else:
            Prev_Stud = self.student_list[searchPosition]
            updated_student = self.updatingData(searchPosition, Prev_Stud)
            student = Student(updated_student["name"], updated_student["phone"], updated_student["email"], updated_student["gender"])

            del self.student_list[searchPosition]
            if updated_student["name"] == Prev_Stud.name:
                self.student_list.insert(searchPosition, student)
            else:
                updatePosition = 0
                for item in self.student_list:
                    if updated_student["name"] > item.name:
                        updatePosition += 1
                    else:
                        break
                self.student_list.insert(updatePosition, student)
            print("Element was updated")
            return