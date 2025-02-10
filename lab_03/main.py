from items.student_list import student_list
from items.utils import CSV_operations

def main():
    studlist = student_list()
    file = CSV_operations(studlist)
    file.loadCSV()
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                studlist.addNewElement(studlist.addingNew())
                studlist.prinList()
            case "U" | "u":
                print("Existing element will be updated")
                studlist.updateElement(input("Please enter name to be updated: "))
                studlist.prinList()
            case "D" | "d":
                print("Element will be deleted")
                studlist.deleteElement(input("Please enter name to be delated: "))
            case "P" | "p":
                print("List will be printed")
                studlist.prinList()
            case "X" | "x":
                file.saveCSV()
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()