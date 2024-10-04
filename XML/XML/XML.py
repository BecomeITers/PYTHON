import xml.etree.ElementTree as ET
from xml.dom import minidom

# File path for XML
FILE_PATH = 'students.xml'

def create_xml():
    """Create the initial XML file with student data."""
    students = ET.Element("students")
    student_data = [
        {"id": "001", "name": "Nguyễn Văn A", "dob": "2000-01-01", "major": "Công nghệ thông tin"},
        {"id": "002", "name": "Trần Thị B", "dob": "2000-02-02", "major": "Quản trị kinh doanh"},
        {"id": "003", "name": "Phạm Văn C", "dob": "2000-03-03", "major": "Kỹ thuật điện"}
    ]
    for data in student_data:
        student = ET.SubElement(students, "student")
        ET.SubElement(student, "id").text = data["id"]
        ET.SubElement(student, "name").text = data["name"]
        ET.SubElement(student, "dob").text = data["dob"]
        ET.SubElement(student, "major").text = data["major"]
    tree = ET.ElementTree(students)
    with open(FILE_PATH, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)
    print("Tạo tập tin thành công")

def add_student(new_student):
    """Add a new student to the XML file."""
    tree = ET.parse(FILE_PATH)
    root = tree.getroot()
    
    for student in root.findall('student'):
        if student.find('id').text == new_student['id']:
            print(f"ID {new_student['id']} đã tồn tại.")
            return
    
    student = ET.SubElement(root, "student")
    ET.SubElement(student, "id").text = new_student["id"]
    ET.SubElement(student, "name").text = new_student["name"]
    ET.SubElement(student, "dob").text = new_student["dob"]
    ET.SubElement(student, "major").text = new_student["major"]
    
    tree.write(FILE_PATH, encoding="utf-8", xml_declaration=True)
    print("Thêm sinh viên thành công.")

def edit_student(student_id, updated_info):
    """Edit an existing student's information based on ID."""
    tree = ET.parse(FILE_PATH)
    root = tree.getroot()
    
    for student in root.findall('student'):
        if student.find('id').text == student_id:
            student.find('name').text = updated_info.get('name', student.find('name').text)
            student.find('dob').text = updated_info.get('dob', student.find('dob').text)
            student.find('major').text = updated_info.get('major', student.find('major').text)
            tree.write(FILE_PATH, encoding="utf-8", xml_declaration=True)
            print("Cập nhật thông tin sinh viên thành công.")
            return
    print(f"Sinh viên với ID {student_id} không tìm thấy.")

def delete_student(student_id):
    """Delete a student from the XML file based on ID."""
    tree = ET.parse(FILE_PATH)
    root = tree.getroot()
    
    for student in root.findall('student'):
        if student.find('id').text == student_id:
            root.remove(student)
            tree.write(FILE_PATH, encoding="utf-8", xml_declaration=True)
            print("Xóa sinh viên thành công.")
            return
    print(f"Sinh viên với ID {student_id} không tìm thấy.")

def find_students_by_surname(surname):
    """Find students by surname."""
    tree = ET.parse(FILE_PATH)
    root = tree.getroot()
    found_students = []
    
    for student in root.findall('student'):
        if student.find('name').text.startswith(surname):
            student_info = {
                "id": student.find('id').text,
                "name": student.find('name').text,
                "dob": student.find('dob').text,
                "major": student.find('major').text
            }
            found_students.append(student_info)
    
    return found_students

def count_students():
    """Count the total number of students."""
    tree = ET.parse(FILE_PATH)
    root = tree.getroot()
    return len(root.findall('student'))

if __name__ == "__main__":
    create_xml()
    
    new_student = {"id": "004", "name": "Nguyễn Văn D", "dob": "2000-04-04", "major": "Marketing"}
    add_student(new_student)

    edit_student("001", {"name": "Nguyễn Văn A1", "dob": "2000-01-02", "major": "Khoa học máy tính"})

    delete_student("003")

    students_found = find_students_by_surname("Trần")
    print("Sinh viên có họ 'Trần':")
    for student in students_found:
        print(student)

    total_students = count_students()
    print(f"Tổng số lượng sinh viên: {total_students}")
