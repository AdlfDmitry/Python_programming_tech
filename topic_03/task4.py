def insert_in_sorted_list(sorted_list, new_element):
    position = find_insert_position(sorted_list, new_element)
    sorted_list.insert(position, new_element)
    return sorted_list
def find_insert_position(sorted_list, new_element):
    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)
sorted_list = [1, 2, 4, 5, 7, 8, 10]
new_element = 6
print("Sorted list:", sorted_list)
updated_list = insert_in_sorted_list(sorted_list, new_element)
print("Updated list:", updated_list)
