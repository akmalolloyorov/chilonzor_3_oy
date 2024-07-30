from LTS.student.student import Student, int_input


class Teacher(Student):
    def show_menu_teacher(self, username: str, teacher_file: dict) -> str:
        text = """
        1. View Students List
        2. View Lessons
        3. Add New Lesson
        4. Change Lesson Topic
        5. Grade Students
        6. Update Student Grade
        7. change password
        8. Personal Information
        9. Logout
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.view_students_list(username=username, teacher_file=teacher_file)
        elif num == 2:
            self.view_lessons(username=username, teacher_file=teacher_file)
        elif num == 3:
            self.add_new_lesson(username=username, teacher_file=teacher_file)
        elif num == 4:
            self.change_lesson_topic(username=username, teacher_file=teacher_file)
        elif num == 5:
            self.grade_students(username=username, teacher_file=teacher_file)
        elif num == 6:
            self.update_student_grade(username=username, teacher_file=teacher_file)
        elif num == 7:
            self.change_password_teacher(username=username, teacher_file=teacher_file)
        elif num == 8:
            self.personal_information_teacher(username=username, teacher_file=teacher_file)
        else:
            return "num"
        self.show_menu_teacher(username=username, teacher_file=teacher_file)

    def personal_information_teacher(self, username, teacher_file):
        print(f"full name: {teacher_file[username]['name']}")
        print(f"username: {username}")
        print(f"phone number: {teacher_file[username]['phone_number']}")
        for group, directions in teacher_file[username]['group'].items():
            print(f"group: {group}")
            print(f"directions: {directions['direction']}")
            print(f"students: {directions['students']}")
        self.__str__()

    def view_students_list(self, username: str, teacher_file: dict):
        student_file = self.read_to_file(self._student_file)
        group_list: list = []
        if len(teacher_file[username]["group"]) > 0:
            for group in teacher_file[username]["group"].keys():
                group_list.append(group)
            group = self.list_choice(group_list)
            if len(teacher_file[username]["group"][group]['students']) > 0:
                for i in teacher_file[username]["group"][group]['students']:
                    print(f"Student name: {student_file[i]["student_name"]}")
                return
            else:
                print("no find students")
        else:
            print("No find students")
            return

    def view_lessons(self, username: str, teacher_file: dict):
        direction_list: list = []
        if len(teacher_file[username]["direction"]) > 0:
            for direction in teacher_file[username]["direction"].keys():
                direction_list.append(direction)
            direction: str = self.list_choice(direction_list)
            for group, v in teacher_file[username]['group'].items():
                if direction in v['direction']:
                    print(f"group: {group}")
            print(f"direction: {direction}")
            if len(teacher_file[username]["direction"][direction]) > 0:
                print("lessons:")
                count = 0
                for lesson in teacher_file[username]["direction"][direction].keys():
                    count += 1
                    print(f"    {count}.{lesson}")
                return
            else:
                print("no find lessons.")
        else:
            print("No find directions.")

    def add_new_lesson(self, username: str, teacher_file: dict):
        student_file: dict = self.read_to_file(self._student_file)
        if len(teacher_file[username]["direction"]) > 0:
            direction_list: list = []
            for direction in teacher_file[username]["direction"].keys():
                direction_list.append(direction)
            direction: str = self.list_choice(direction_list)
            gr: str = "none"
            for group, directions in teacher_file[username]["group"].items():
                if direction in directions['direction']:
                    gr: str = group
            lesson_name: str = input("Enter the lesson name: ")
            lesson_time: str = input("Enter the lesson time (e.g., 22.07.2024): ")
            lesson = {
                lesson_name: {
                    "lesson_time": lesson_time,
                    "students": {}
                }
            }
            teacher_file[username]['direction'][direction].update(lesson)
            student_group_list: list = []
            student_direction_list: list = []
            for user, value in student_file.items():
                if value['group'] == gr:
                    if direction in value['direction']:
                        student_direction_list.append(user)
                    else:
                        student_group_list.append(user)
            if len(student_direction_list) > 0 or len(student_group_list) > 0:
                if len(student_direction_list) > 0:
                    for student in student_direction_list:
                        user = {student: "none"}
                        lesson = {lesson_name: {
                            "lesson_time": lesson_time,
                            'grade': "none"
                        }}
                        teacher_file[username]['direction'][direction][lesson_name]['students'].update(user)
                        student_file[student]['direction'][direction].update(lesson)
                if len(student_group_list) > 0:
                    for student in student_group_list:
                        user = {student: "none"}
                        d = {direction: {
                            lesson_name: {
                                "lesson_time": lesson_time,
                                'grade': "none"
                            }}}
                        teacher_file[username]['direction'][direction][lesson_name]['students'].update(user)
                        student_file[student]['direction'].update(d)

                self.write_to_file(self._student_file, student_file)
                self.write_to_file(self._teacher_file, teacher_file)
                return
            else:
                print("no find students in group")
        else:
            print("No find directions.")

    def change_lesson_topic(self, username: str, teacher_file: dict):
        s: dict = self.read_to_file(self._student_file)
        if len(teacher_file[username]["direction"]) > 0:
            direction_list: list = []
            for direction in teacher_file[username]["direction"].keys():
                direction_list.append(direction)
            direction: str = self.list_choice(direction_list)
            lesson_list: list = []
            if len(teacher_file[username]["direction"][direction]) > 0:
                for lesson in teacher_file[username]["direction"][direction].keys():
                    lesson_list.append(lesson)
                old: str = self.list_choice(lesson_list)
                name: str = input("Enter the new lesson name: ")
                new_lesson: dict = {
                    name: {
                        "lesson_time": teacher_file[username]["direction"][direction][old]["lesson_time"],
                        "students": teacher_file[username]["direction"][direction][old]["students"]
                    }
                }
                for user in teacher_file[username]['direction'][direction][old]['students'].keys():
                    s[user]['direction'][direction].update({name: s[user]['direction'][direction][old]})
                    del s[user]['direction'][direction][old]

                teacher_file[username]["direction"][direction].update(new_lesson)
                del teacher_file[username]["direction"][direction][old]
                self.write_to_file(self._student_file, s)
                self.write_to_file(self._teacher_file, teacher_file)
                return
            else:
                print("no find lessons.")
                return
        else:
            print("No find directions.")
        return

    def grade_students(self, username: str, teacher_file: dict):
        student_file: dict = self.read_to_file(self._student_file)
        direction_list: list = []
        if len(teacher_file[username]['direction']) > 0:
            for direction in teacher_file[username]['direction'].keys():
                direction_list.append(direction)
            direction: str = self.list_choice(direction_list)
            lesson_list: list = []
            if len(teacher_file[username]['direction'][direction]) > 0:
                for lesson in teacher_file[username]['direction'][direction].keys():
                    lesson_list.append(lesson)
                lesson: str = self.list_choice(lesson_list)
                for user in teacher_file[username]["direction"][direction][lesson]['students'].keys():
                    if teacher_file[username]["direction"][direction][lesson]['students'][user] == "none":
                        grade = self.grade_input(f"Give a grade to {student_file[user]['student_name']}: ")
                        teacher_file[username]["direction"][direction][lesson]['students'][user] = grade
                        student_file[user]['direction'][direction][lesson]['grade'] = grade
                    else:
                        print(f"A grade has already been assigned to {student_file[user]['student_name']}")
                self.write_to_file(self._student_file, student_file)
                self.write_to_file(self._teacher_file, teacher_file)
                return
            else:
                print("no find lessons.")
                return
        else:
            print("No find directions.")
            return

    def update_student_grade(self, username: str, teacher_file: dict):
        student_file = self.read_to_file(self._student_file)
        direction_list: list = []
        if len(teacher_file[username]['direction']) > 0:
            for direction in teacher_file[username]['direction'].keys():
                direction_list.append(direction)
            direction: str = self.list_choice(direction_list)
            lesson_list: list = []
            if len(teacher_file[username]['direction'][direction]) > 0:
                for lesson in teacher_file[username]['direction'][direction].keys():
                    lesson_list.append(lesson)
                lesson: str = self.list_choice(lesson_list)
                user_list: list = []
                name_list: list = []
                for user in teacher_file[username]["direction"][direction][lesson]['students'].keys():
                    user_list.append(user)
                    name_list.append(student_file[user]['student_name'])
                name = self.list_choice(name_list)
                f_index = name_list.index(name)
                user = user_list[f_index]
                print(f"Previous grade - {teacher_file[username]['direction'][direction][lesson]['students'][user]}")
                grade = self.grade_input("Enter new grade: ")
                teacher_file[username]["direction"][direction][lesson]['students'][user] = grade
                student_file[user]['direction'][direction][lesson]['grade'] = grade
                self.write_to_file(self._student_file, student_file)
                self.write_to_file(self._teacher_file, teacher_file)
                return
            else:
                print("no find lessons.")
                return
        else:
            print("No find directions.")
            return

    def change_password_teacher(self, username: str, teacher_file: dict):
        self.change_password_student(username=username, file=teacher_file, write_file=self._teacher_file)
