import hashlib
import random

from LTS.admin.subject_crud import SubjectCurd, int_input


class TeacherCrud(SubjectCurd):
    def teacher_crud(self, teacher_file, student_file) -> str:
        text = """
            1. Add New Teacher
            2. View All Teachers
            3. Update Teacher Information
            4. Delete Teacher
            5. Teacher password change
            6. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.add_teacher(teacher_file=teacher_file)
        elif num == 2:
            self.view_teachers(teacher_file=teacher_file, student_file=student_file)
        elif num == 3:
            self.update_teacher_info(teacher_file=teacher_file, student_file=student_file)
        elif num == 4:
            self.delete_teacher(teacher_file=teacher_file, student_file=student_file)
        elif num == 5:
            self.change_teacher_password(teacher_file=teacher_file, student_file=student_file)
        else:
            return "num"
        self.teacher_crud(teacher_file=teacher_file, student_file=student_file)

    def change_teacher_password(self, teacher_file, student_file):
        my_list: list = ['teacher']
        m_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, my_list)
        teacher: str = m_list[0]
        self.change_password_teacher(username=teacher, teacher_file=teacher_file)

    def add_teacher(self, teacher_file: dict):
        teacher_name = input("Enter teacher name: ").title()
        teacher_phone = self.phone_input("Enter teacher phone: ")
        num: int = random.randint(100000, 999999)
        while f"TM{num}" in teacher_file.keys():
            num: int = random.randint(100000, 999999)
        username = f"TM{num}"
        parol: int = random.randint(1000000, 9999999)
        while parol in teacher_file.values():
            parol: int = random.randint(1000000, 9999999)
        p: str = hashlib.sha256(str(parol).encode()).hexdigest()
        user: dict = {
            username: {
                "password": p,
                "name": teacher_name,
                "phone_number": teacher_phone,
                "group": {},
                "direction": {}
            }
        }
        teacher_file.update(user)
        self.write_to_file(self._teacher_file, teacher_file)
        print(f"Teacher: username - {username}, password - {parol} ")

    def view_teachers(self, teacher_file: dict, student_file: dict):
        my_list: list = ['teacher']
        m_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, my_list)
        teacher: str = m_list[0]
        self.personal_information_teacher(username=teacher, teacher_file=teacher_file)

    def update_teacher_info(self, teacher_file: dict, student_file: dict):
        my_list: list = ['teacher']
        m_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, my_list)
        teacher: str = m_list[0]
        new_name: str = input("New teacher name: ").title()
        teacher_phone: int = self.phone_input("New teacher phone: ")
        num: int = random.randint(100000, 999999)
        while f"TM{num}" in teacher_file.keys():
            num: int = random.randint(100000, 999999)
        username: str = f"TM{num}"
        parol: int = random.randint(1000000, 9999999)
        while parol in teacher_file.values():
            parol: int = random.randint(1000000, 9999999)
        p: str = hashlib.sha256(str(parol).encode()).hexdigest()
        user: dict = {
            username: teacher_file[teacher]
        }
        teacher_file.update(user)
        teacher_file[username]["name"] = new_name
        teacher_file[username]["phone_number"] = teacher_phone
        teacher_file[username]["password"] = p
        del teacher_file[teacher]
        self.write_to_file(self._teacher_file, teacher_file)
        print(f"Teacher: username - {username}, password - {parol} ")

    def delete_teacher(self, teacher_file, student_file):
        my_list: list = ['teacher']
        m_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, my_list)
        teacher: str = m_list[0]
        del teacher_file[teacher]
        self.write_to_file(self._teacher_file, teacher_file)
