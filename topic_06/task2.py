list = [{'name':"Alex", 'mark':9}, 
         {'name':"John", 'mark':8},
         {'name':"Mike", 'mark':6},
         {'name':"Kate", 'mark':10}]

while True:
    sortingMethod=input("Select sorting method: Enter 'n - name' or 'm- mark' or 'p- print unsorted' or Enter 'exit' to stop program:").lower()
    if sortingMethod == "exit":
        exit(0)
    elif sortingMethod =="n":
         for name in sorted(list, key = lambda elem : elem["name"]):
            print(f"Name — {name['name']} | Mark — {name['mark']}")
            
    elif sortingMethod=="m":
        for name in sorted(list, key = lambda elem : elem["mark"]):
            print(f"Name — {name['name']} | Mark — {name['mark']}")
    elif sortingMethod =="p":
         print(list)
