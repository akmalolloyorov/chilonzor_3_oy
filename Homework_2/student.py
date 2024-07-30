import hashlib

from json_manager import JsonManager, int_input


class Student(JsonManager):
    def show_menu_student(self, username):
        text = """
        1. See the class schedule
        2. View the grade
        3. change the password
        4. personal information
        5. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 2:
            self.see_class_schedule(username)
            self.show_menu_student(username)
        elif num == 1:
            self.view_grade(username)
            self.show_menu_student(username)
        elif num == 3:
            self.change_password(username)
            self.show_menu_student(username)
        elif num == 4:
            self.personal_information(username)
            self.show_menu_student(username)
        else:
            return 0

    def change_password(self, username):
        new_parol = input("Enter your new password: ")
        p = hashlib.sha256(new_parol.encode()).hexdigest()
        student_file: dict = self.read_to_file(self._student_file)
        student_file[username]["password"] = p
        self.write_to_file(self._student_file, student_file)
        print("Password changed successfully")

    def personal_information(self, username):
        student_file: dict = self.read_to_file(self._student_file)
        print(f"Name: {student_file[username]['student_name']}")
        print(f"Group: {student_file[username]['group']}")
        print(f"Teacher: {student_file[username]['teacher']}")
        for direction in student_file[username]['direction'].keys():
            print(f"Direction: {direction}")

    def see_class_schedule(self, username):
        student_file: dict = self.read_to_file(self._student_file)
        if len(student_file[username]["direction"]) > 0:
            direction_list = []
            for direction in student_file[username]["direction"].keys():
                direction_list.append(direction)
            print("choice direction")
            direction = self.list_choice(direction_list)
            if len(student_file[username]["direction"][direction]) > 0:
                lesson_list = []
                for lesson in student_file[username]["direction"][direction].keys():
                    lesson_list.append(lesson)
                print("choice lesson")
                lesson = self.list_choice(lesson_list)
                if student_file[username]["direction"][direction][lesson]['grade'] == "none":
                    print("You have not been graded yet")
                else:
                    print(f"Grade: {student_file[username]['direction'][direction][lesson]['grade']}")
            else:
                print("You don't have any lesson in this direction")
        else:
            print("You don't have any direction")

    def view_grade(self, username):
        student_file: dict = self.read_to_file(self._student_file)
        if len(student_file[username]["direction"]) > 0:
            direction_list = []
            for direction in student_file[username]["direction"].keys():
                direction_list.append(direction)
            print("choice direction")
            direction = self.list_choice(direction_list)
            if len(student_file[username]["direction"][direction]) > 0:
                lesson_list = []
                for lesson in student_file[username]["direction"][direction].keys():
                    lesson_list.append(lesson)
                print("choice lesson")
                lesson = self.list_choice(lesson_list)
                print(f"Lesson name : {student_file[username]["direction"][direction][lesson]['lesson_name']}")
                print(f"Lesson time : {student_file[username]["direction"][direction][lesson]['lesson_time']}")
            else:
                print("You don't have any lesson in this direction")
        else:
            print("You don't have any direction")
