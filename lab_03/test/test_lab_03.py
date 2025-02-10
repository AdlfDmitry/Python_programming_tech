import pytest
from ..items.student_list import student_list
from ..items.utils import CSV_operations
from unittest.mock import patch
import io


def test_addNewElement():
    stud_list = student_list()
    Student_1 = {"name": "Delta", "phone": "36227383", "email": "delta@mail", "gender": "male"}
    Student_2 = {"name": "Echo", "phone": "63278131", "email": "echo@mail", "gender": "female"}
    stud_list.addNewElement(Student_1)
    stud_list.addNewElement(Student_2)
    assert stud_list.student_list[0].name == "Delta"
    assert stud_list.student_list[1].name == "Echo"
    assert len(stud_list.student_list) == 2

def test_deleteElement():
    stud_list = student_list()
    Student_1 = {"name": "Delta", "phone": "36227383", "email": "delta@mail", "gender": "male"}
    stud_list.addNewElement(Student_1)
    stud_list.deleteElement("Delta")
    assert len(stud_list.student_list) == 0
    stud_list.addNewElement(Student_1)
    stud_list.deleteElement("Foxtrot")
    assert len(stud_list.student_list) == 1

def test_saveloadCSV(tmp_path):
    file_path = tmp_path / "test.csv"
    
    stud_list = student_list()
    file = CSV_operations(stud_list)
    file.file = str(file_path) 

    Student_2 = {"name": "Echo", "phone": "63278131", "email": "echo@mail", "gender": "female"}
    stud_list.addNewElement(Student_2)
    file.saveCSV()
    
    stud_list_loaded = student_list()
    file_loaded = CSV_operations(stud_list_loaded)
    file_loaded.file = str(file_path)
    file_loaded.loadCSV()

    assert len(stud_list_loaded.student_list) == 1
    assert stud_list_loaded.student_list[0].name == "Echo"