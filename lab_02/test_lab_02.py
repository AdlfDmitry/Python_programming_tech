import pytest

@pytest.fixture
def mock_student_list():
    return []

def test_add_new_student(mock_student_list):
    add_new_student_mock("John", "123456789", "john@example.com", "male", mock_student_list)
    assert len(mock_student_list) == 1
    assert mock_student_list[0]["name"] == "John"

def test_delete_student(mock_student_list):
    mock_student_list.append({"name": "John", "phone": "123456789", "email": "john@example.com", "gender": "male"})
    delete_student_mock("John", mock_student_list)
    assert len(mock_student_list) == 0

def test_update_student(mock_student_list):
    mock_student_list.append({"name": "John", "phone": "123456789", "email": "john@example.com", "gender": "male"})
    update_student_mock("John", "Johnny", "987654321", "johnny@example.com", "male", mock_student_list)
    assert mock_student_list[0]["name"] == "Johnny"
    assert mock_student_list[0]["phone"] == "987654321"
    assert mock_student_list[0]["email"] == "johnny@example.com"

def add_new_student_mock(name, phone, email, gender, student_list):
    new_student = {"name": name, "phone": phone, "email": email, "gender": gender}
    insert_position = next((i for i, student in enumerate(student_list) if name < student["name"]), len(student_list))
    student_list.insert(insert_position, new_student)

def delete_student_mock(name, student_list):
    student_list[:] = [student for student in student_list if student["name"] != name]

def update_student_mock(old_name, new_name, new_phone, new_email, new_gender, student_list):
    student = next((s for s in student_list if s["name"] == old_name), None)
    if student:
        student["name"] = new_name
        student["phone"] = new_phone
        student["email"] = new_email
        student["gender"] = new_gender
