def dictionary_operations():
    my_dict = {
        'name': 'Dmitry',
        'age': 18,
        'city': 'Kyiv'
    }
    print("Starting dictionary:", my_dict)
    my_dict.update({'age': 19, 'job': 'Cybersecurity'})
    print("Dictionary  updated:", my_dict)
    del my_dict['city']
    print("Dictionary after deleting 'city':", my_dict)
    my_dict_copy = my_dict.copy()
    my_dict.clear()
    print("Dictionary after clear():", my_dict)
    print("Keys of the dictionary copy:", my_dict_copy.keys())
    print("Values of the dictionary copy:", my_dict_copy.values())
    print("Items of the dictionary copy:", my_dict_copy.items())
dictionary_operations()
