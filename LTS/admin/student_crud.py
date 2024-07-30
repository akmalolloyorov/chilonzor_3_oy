from LTS.admin.group_crud import GroupCrud, int_input
import random
import hashlib


class StudentCrud(GroupCrud):
    def student_crud(self, teacher_file: dict, student_file: dict):
        text = """
        1. Add Student
        2. View All Students
        3. Update Student Information
        4. Delete Student
        5. View Personal Information
        6. View Course Grades
        7. View lessons schedule
        8. Change password
        9. Grade Students
        10. Update Student Grade
        11. Exit
        """
        print(text)
        num = int_input("Enter your choice: ")

        if num == 1:
            self.add_student(teacher_file, student_file)
        elif num == 2:
            self.view_all_students(student_file)
        elif num == 3:
            self.update_student_info(student_file)
        elif num == 4:
            self.delete_student(teacher_file=teacher_file, student_file=student_file)
        elif num == 5:
            self.view_personal_info_a(student_file)
        elif num == 6:
            self.view_course_grades_a(student_file)
        elif num == 7:
            self.view_lessons_schedule_a(student_file=student_file)
        elif num == 8:
            self.change_p(student_file=student_file)
        elif num == 9:
            self.grade_students_teacher(teacher_file, student_file)
        elif num == 10:
            self.update_student_grade_teacher(teacher_file, student_file)
        else:
            return "num"
        self.student_crud(teacher_file=teacher_file, student_file=student_file)

    def update_student_grade_teacher(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher", "direction", 'lesson', 'user']
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        user = my_list[0]
        self.update_student_grade(username=user, teacher_file=teacher_file)

    def grade_students_teacher(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher", "direction", 'lesson', 'user']
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        user = my_list[0]
        self.grade_students(username=user, teacher_file=teacher_file)

    def add_student(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher", "direction"]
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher: str = my_list[0]
        direction: str = my_list[1]
        num: int = random.randint(100000, 999999)
        while f"TM{num}" in teacher_file.keys():
            num: int = random.randint(100000, 999999)
        username = f"TM{num}"
        parol: int = random.randint(1000000, 9999999)
        while parol in teacher_file.values():
            parol: int = random.randint(1000000, 9999999)
        p: str = hashlib.sha256(str(parol).encode()).hexdigest()
        group = 0
        student_name: str = input("Student Name: ").title()
        phone: int = self.phone_input("Enter a phone number: ")
        for gr, value in teacher_file[teacher]['group'].items():
            if direction in value['direction']:
                group = gr
        user: dict = {
            username: {
                'password': p,
                "student_name": student_name,
                "phone_number": phone,
                "group": group,
                "teacher": teacher_file[teacher]['name'],
                "direction": {direction: {}}
            }
        }
        student_file.update(user)
        self.write_to_file(self._student_file, student_file)
        teacher_file[teacher]['group'][group]['students'].append(username)
        self.write_to_file(self._teacher_file, teacher_file)

    def view_all_students(self, student_file: dict) -> None:
        for i, j in student_file.items():
            print(f"name: {j["student_name"]}, username: {i}")
        self.__str__()

    def update_student_info(self, student_file: dict) -> None:
        user = self.user_for(student_file=student_file)
        new_name = input("Enter new full name: ").title()
        new_phone = self.phone_input("Enter new phone number: ")
        student_file[user]["student_name"] = new_name
        student_file[user]["student_phone"] = new_phone
        self.write_to_file(self._student_file, student_file)

    def delete_student(self, teacher_file: dict, student_file: dict) -> None:
        user: str = self.user_for(student_file=student_file)
        for teacher, value in teacher_file.items():
            for g, i in value['group'].items():
                for ll in i.values():
                    for m in ll:
                        if m == user:
                            del teacher_file[teacher]['group'][g]['students'][ll.index(user)]
        for teacher, value in teacher_file.items():
            for direction, d_value in value['direction'].items():
                for lesson, l_values in d_value.items():
                    if 'students' in l_values:
                        if user in l_values['students']:
                            del l_values['students'][user]
        del student_file[user]
        self.write_to_file(self._student_file, student_file)
        self.write_to_file(self._teacher_file, teacher_file)

    def view_personal_info_a(self, student_file: dict) -> None:
        user = self.user_for(student_file=student_file)
        self.view_personal_info(username=user, student_file=student_file)

    def view_course_grades_a(self, student_file: dict) -> None:
        user: str = self.user_for(student_file=student_file)
        self.view_course_grades(username=user, student_file=student_file)

    def view_lessons_schedule_a(self, student_file) -> None:
        user: str = self.user_for(student_file=student_file)
        self.view_lessons_schedule(username=user, student_file=student_file)

    def user_for(self, student_file: dict) -> str:
        student_name_list: list = []
        student_user_list: list = []
        for user, value in student_file.items():
            student_user_list.append(user)
            student_name_list.append(value['student_name'])
        student_name: str = self.list_choice(student_name_list)
        s_index: int = student_name_list.index(student_name)
        user: str = student_user_list[s_index]
        return user

    def change_p(self, student_file: dict) -> None:
        user: str = self.user_for(student_file)
        self.change_password_student(username=user, file=student_file, write_file=self._student_file)
