list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "gender":"male"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "gender":"female"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "gender":"male"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "gender":"male"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Gender is " + elem["gender"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    gender = input("Please enter student gender: ")
    newItem = {"name": name, "phone": phone, "email":email, "gender":gender}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1 
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    updateStudent = None
    for student in list:
        if name == student["name"]:
            updateStudent = student
            break
        if not updateStudent:
         print("Student not found")
         return 
        print("Current details - Name: {updateStudent['name']}, Phone: {updateStudent['phone']}, Email: {updateStudent['email']}, Gender: {updateStudent['gender']}")
    new_name = input(f"Enter new name (leave empty to keep '{updateStudent['name']}'): ") or updateStudent["name"]
    new_phone = input(f"Enter new phone (leave empty to keep '{updateStudent['phone']}'): ") or updateStudent["phone"]
    new_email = input(f"Enter new email (leave empty to keep '{updateStudent['email']}'): ") or updateStudent["email"]
    new_gender = input(f"Enter new gender (leave empty to keep '{updateStudent['gender']}'): ") or updateStudent["gender"]
    updatedStudent = {"name": new_name, "phone": new_phone, "email": new_email, "gender": new_gender}
    list.remove(updateStudent)
    insertPosition = 0
    for student in list:
        if updatedStudent["name"] > student["name"]:
            insertPosition = insertPosition + 1
        else:
            break
        list.insert(insertPosition, updatedStudent)
        print("Student information has been updated succesfuly")
        return
    
def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
main()