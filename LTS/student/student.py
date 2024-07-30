import hashlib

from LTS.json_manager import JsonManager, int_input


class Student(JsonManager):
    def show_menu_student(self, username: str, student_file: dict) -> str:
        text = """
        1. View Personal Information
        2. View Course Grades
        3. View lessons schedule
        4. Change password
        5. Logout
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.view_personal_info(username=username, student_file=student_file)
        elif num == 2:
            self.view_course_grades(username=username, student_file=student_file)
        elif num == 3:
            self.view_lessons_schedule(username=username, student_file=student_file)
        elif num == 4:
            self.change_password_student(username=username, file=student_file, write_file=self._student_file)
        else:
            return "num"
        self.show_menu_student(username=username, student_file=student_file)

    def view_personal_info(self, username: str, student_file: dict):
        self.__str__()
        text = f"""
        full name - {student_file[username]['student_name']}
        phone number - {student_file[username]['phone_number']}
        Group - {student_file[username]['group']}"""
        print(text)
        try:
            [print(f"        direction - {i}") for i in student_file[username]['direction'].keys()]
        except KeyError:
            print("You don't have any direction")

    def view_course_grades(self, username: str, student_file: dict):
        direction_list: list = []
        if len(student_file[username]['direction']) > 0:
            for direction in student_file[username]['direction'].keys():
                direction_list.append(direction)
            direction = self.list_choice(direction_list)
            lesson_list: list = []
            if len(student_file[username]['direction'][direction]) > 0:
                for lesson in student_file[username]['direction'][direction].keys():
                    lesson_list.append(lesson)
                lesson = self.list_choice(lesson_list)
                if student_file[username]['direction'][direction][lesson]['grade'] == "none":
                    return print(f"{direction} -> {lesson} -> grade: Grade not yet assigned")
                else:
                    text = f"""
        group name - {student_file[username]['group']}
        direction name - {direction}  
        lesson name - {lesson}
        grade - {student_file[username]['direction'][direction][lesson]['grade']}
                    """
                    return print(text)
            else:
                print("You don't have any lesson in this direction")
        else:
            print("You don't have any direction")

    def view_lessons_schedule(self, username: str, student_file: dict):
        direction_list: list = []
        if len(student_file[username]['direction']) > 0:
            for direction in student_file[username]['direction'].keys():
                direction_list.append(direction)
            direction = self.list_choice(direction_list)
            lesson_list = []
            if len(student_file[username]['direction'][direction]) > 0:
                for lesson in student_file[username]['direction'][direction].keys():
                    lesson_list.append(lesson)
                lesson = self.list_choice(lesson_list)
                text = f"""
                        group name - {student_file[username]['group']}
                        direction name - {direction}  
                        lesson name - {lesson}
                        lesson time - {student_file[username]['direction'][direction][lesson]['lesson_time']}
                                    """
                return print(text)
            else:
                print("You don't have any lesson in this direction")
        else:
            print("You don't have any direction")

    def change_password_student(self, username: str, file: dict, write_file: str):
        old_parol: str = input("Enter the old password: ")
        o_p: str = hashlib.sha256(old_parol.encode()).hexdigest()
        new_parol: str = input("Enter the new password: ")
        n_p: str = hashlib.sha256(new_parol.encode()).hexdigest()
        if file[username]['password'] == o_p:
            file[username]['password'] = n_p
            self.write_to_file(write_file, file)
            print("Password changed successfully")
        else:
            print("Wrong old password")
