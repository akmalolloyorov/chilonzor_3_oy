from json_manager import JsonManager, int_input


class Teacher(JsonManager):

    def show_menu_teacher(self, username):
        text = """
        1. Student evaluation 
        2. Change a student's grade
        3. Add subject
        4. Personal information
        5. View the class schedule
        6. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.student_evaluation(username)
            self.show_menu_teacher(username)
        elif num == 2:
            self.change_grade(username)
            self.show_menu_teacher(username)
        elif num == 3:
            self.add_subject_teacher(username)
            self.show_menu_teacher(username)
        elif num == 4:
            self.personal_i_teacher(username)
            self.show_menu_teacher(username)
        elif num == 5:
            self.view_class_schedule_teacher(username)
            self.show_menu_teacher(username)
        else:
            return 0

    def view_class_schedule_teacher(self, username):
        teacher_file: dict = self.read_to_file(self._teacher_file)
        group, direction, lesson = self.for_function_teacher(username)
        text = f"""
        Class topic - {teacher_file[username]['group'][group][direction][lesson]['lesson_name']}
        Class time - {teacher_file[username]['group'][group][direction][lesson]['lesson_time']}
        """
        print(text)

    def personal_i_teacher(self, username):
        student_file: dict = self.read_to_file(self._student_file)
        teacher_file: dict = self.read_to_file(self._teacher_file)
        print(f"Teacher's name - {teacher_file[username]['name']}")
        print(f"Teacher's phone number - {teacher_file[username]['phone_number']}")
        if len(teacher_file[username]["group"]) > 0:
            for groups, directions in teacher_file[username]["group"].items():
                print(f"Teacher group - {groups}⬇️")
                for user, value in student_file.items():
                    if value['group'] == groups:
                        print(f"Teacher student - {student_file[user]['student_name']}")
                if len(directions) > 0:
                    for direction in directions:
                        print(f"Teacher direction - {direction}")

        else:
            print("Teacher has no group.")

    def student_evaluation(self, username):
        teacher_file = self.read_to_file(self._teacher_file)
        student_file = self.read_to_file(self._student_file)
        print("COMING SOON")
        group, direction, lesson = self.for_function_teacher(username)
        print(f'{group}-group, {direction}-direction, {lesson}-lesson.')
        if len(teacher_file[username]["group"][group][direction][lesson]['students']) > 0:
            for student in teacher_file[username]["group"][group][direction][lesson]['students'].keys():
                if teacher_file[username]["group"][group][direction][lesson]['students'][student] == "none":
                    s = student_file[student]['student_name']
                    grade = self.grade_input(f"Enter grade for: {s}: ")
                    teacher_file[username]["group"][group][direction][lesson]['students'][student] = grade
                    student_file[student]['direction'][direction][lesson]['grade'] = grade
        else:
            print("student were previously assessed.")
        self.write_to_file(self._teacher_file, teacher_file)
        self.write_to_file(self._student_file, student_file)

    def change_grade(self, username):
        teacher_file = self.read_to_file(self._teacher_file)
        student_file = self.read_to_file(self._student_file)
        print("COMING SOON")
        group, direction, lesson = self.for_function_teacher(username)
        print(f'{group}-group, {direction}-direction, {lesson}-lesson.')
        if len(teacher_file[username]["group"][group][direction][lesson]['students']) > 0:
            for student in teacher_file[username]["group"][group][direction][lesson]['students'].keys():
                if teacher_file[username]["group"][group][direction][lesson]['students'][student] != "none":
                    s = student_file[student]['student_name']
                    grade = self.grade_input(f"Change {s}'s grade: ")
                    teacher_file[username]["group"][group][direction][lesson]['students'][student] = grade
                    student_file[student]['direction'][direction][lesson]['grade'] = grade
        else:
            print("Students have not been graded yet.")
        self.write_to_file(self._teacher_file, teacher_file)
        self.write_to_file(self._student_file, student_file)

    def for_function_teacher(self, username):
        teacher_file = self.read_to_file(self._teacher_file)
        group_list: list = []
        try:
            if len(teacher_file[username]['group']) > 0:
                for group in teacher_file[username]["group"].keys():
                    group_list.append(group)
                print("choice group")
                group = self.list_choice(group_list)
                direction_list: list = []
                if len(teacher_file[username]["group"][group]) > 0:
                    for direction in teacher_file[username]["group"][group].keys():
                        direction_list.append(direction)
                    print("choice direction")
                    direction = self.list_choice(direction_list)
                    lesson_list: list = []
                    if len(teacher_file[username]["group"][group][direction]) > 0:
                        for lesson in teacher_file[username]["group"][group][direction].keys():
                            lesson_list.append(lesson)
                        print("choice lesson")
                        lesson = self.list_choice(lesson_list)
                        return group, direction, lesson
                    else:
                        print("NO LESSON")
                        return
                else:
                    print("NO DIRECTION")
                    return
            else:
                print("NO GROUP")
                return
        except KeyError:
            print("An error occurred in the system; it will be resolved soon..")
            return self.show_menu_teacher(username)

    def add_subject_teacher(self, username):
        students = self.read_to_file(self._student_file)
        teachers = self.read_to_file(self._teacher_file)
        try:
            print('choice teacher')
            group_list = []
            if len(teachers[username]["group"]) > 0:
                for i in teachers[username]["group"].keys():
                    group_list.append(i)
                print("choice group")
                gr = self.list_choice(group_list)
                direction_list = []
                if len(teachers[username]["group"][gr]) > 0:
                    for i in teachers[username]["group"][gr].keys():
                        direction_list.append(i)
                    print("choice direction")
                    direction = self.list_choice(direction_list)
                    count_list = []
                    if len(teachers[username]["group"][gr][direction]) > 0:
                        for i in teachers[username]["group"][gr][direction].keys():
                            count_list.append(i)
                    else:
                        count_list = []
                    subject_name = input("Subject name: ")
                    subject_time = input("Subject time(exp: 22.07.2024): ")

                    teachers[username]["group"][gr][direction][f"lesson_{len(count_list) + 1}"] = {
                        "lesson_time": subject_time,
                        "lesson_name": subject_name,
                        "students": {}
                    }
                    user_list = []
                    for i, j in students.items():
                        if j["group"] == gr:
                            if direction in j["direction"].keys():
                                user_list.append(i)
                    if len(user_list) > 0:
                        for i in user_list:
                            lesson = f"lesson_{len(count_list) + 1}"
                            user = {
                                lesson: {
                                    "lesson_time": subject_time,
                                    "lesson_name": subject_name,
                                    "grade": "none"
                                }
                            }
                            students[i]["direction"][direction].update(user)
                        for i, j in students.items():
                            if j["group"] == gr:
                                if direction in j["direction"].keys():
                                    user = {i: "none"}
                                    teachers[username]["group"][gr][direction][f"lesson_{len(count_list) + 1}"][
                                        "students"].update(user)
                        self.write_to_file(self._teacher_file, teachers)
                        self.write_to_file(self._student_file, students)
                    else:
                        print('There are no students in your group')
                else:
                    print('There is no direction in your group')
            else:
                print('You have not been assigned a group yet')

        except Exception as e:
            print(e)


