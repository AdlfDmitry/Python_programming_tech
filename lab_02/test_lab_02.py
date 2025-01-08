import pytest
from lab_02 import list, addNewElement, deleteElement, updateElement

def test_add_new_element(monkeypatch):
    list.clear()
    inputs = iter(['Charlie', '111', 'charlie@mail', 'male'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    addNewElement()
    assert len(list) == 1
    assert list[0]["name"] == "Charlie"
    assert list[0]["phone"] == "111"
    assert list[0]["email"] == "charlie@mail"
    assert list[0]["gender"] == "male"

def test_delete_element(monkeypatch):

    list.clear()
    list.append({"name": "Alice", "phone": "123", "email": "alice@mail", "gender": "female"})
    list.append({"name": "Bob", "phone": "222", "email": "bob@mail", "gender": "male"})

    monkeypatch.setattr('builtins.input', lambda _: 'Alice')    
    deleteElement()
    assert len(list) == 1
    assert list[0]["name"] == "Bob"
    
    monkeypatch.setattr('builtins.input', lambda _: 'NonExistent')
    deleteElement()
    assert len(list) == 1 

def test_update_element(monkeypatch):
    list.clear()
    list.append({"name": "Alice", "phone": "123", "email": "alice@mail", "gender": "female"})
    inputs = iter(['Alice', 'Updated Name', '121', 'alice2@mail', 'female'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    updateElement()
    
    assert len(list) == 1
    assert list[0]["name"] == "Updated Name"
    assert list[0]["phone"] == "121"
    assert list[0]["email"] == "alice2@mail"
    assert list[0]["gender"] == "female"

    monkeypatch.setattr('builtins.input', lambda _: 'NonExistent')
    updateElement() 
    assert len(list) == 1 
