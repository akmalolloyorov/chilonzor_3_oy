import random

from teacher import Teacher, int_input
import hashlib

"""
Admin menu:
     1. Subject -> CRUD
     2. Teacher -> CRUD
     3. Group -> CRUD
     4. Student -> CRUD
     5. Manage lessons -> group_name, teacher, time
     6. Show lessons table
     7. Logout
"""


class Admin(Teacher):
    def show_menu_admin(self):
        text = """
        1. Subject -> CRUD
        2. Teacher -> CRUD
        3. Group -> CRUD
        4. Student -> CRUD
        5. Manage lessons subject and show lessons table
        6. logout
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.subject_menu()
            self.show_menu_admin()
        elif num == 2:
            self.teacher_menu()
            self.show_menu_admin()
        elif num == 3:
            self.group_menu()
            self.show_menu_admin()
        elif num == 4:
            self.student_menu()
            self.show_menu_admin()
        elif num == 5:
            self.manage_lessons()
            self.show_menu_admin()
        else:
            return 0

    def subject_menu(self):
        text = """
        1. Add direction
        2. Create subject
        3. Read subjects
        4. Update subject
        5. Delete direction
        6. Exit
        """
        print(text)
        num = int_input('number: ')
        if num == 2:
            self.create_subject()
            self.subject_menu()
        elif num == 1:
            self.add_direction()
            self.subject_menu()
        elif num == 3:
            self.read_subject()
            self.subject_menu()
        elif num == 4:
            self.update_subject()
            self.subject_menu()
        elif num == 5:
            self.delete_direction()
            self.subject_menu()
        else:
            return

    # subject menu for
    def add_direction(self):
        students = self.read_to_file(self._student_file)
        teachers = self.read_to_file(self._teacher_file)
        try:
            teacher_list_user = []
            teacher_list_name = []
            for i, j in teachers.items():
                teacher_list_user.append(i)
                teacher_list_name.append(j["name"])
            if len(teacher_list_user) > 0:
                print('choice teacher')
                teacher_name = self.list_choice(teacher_list_name)
                teacher_user_index = teacher_list_name.index(teacher_name)
                teacher = teacher_list_user[teacher_user_index]
                group_list = []
                for i in teachers[teacher]["group"].keys():
                    group_list.append(i)
                if len(group_list) > 0:
                    print("choice group")
                    gr = self.list_choice(group_list)
                    direction = input("Direction: ")
                    u = {direction: {}}
                    teachers[teacher]["group"][gr].update(u)

                    user_list = []
                    for i, j in students.items():
                        if j["group"] == gr:
                            user_list.append(i)
                    if len(user_list) > 0:
                        for i in user_list:
                            u = {direction: {}}
                            students[i]["direction"].update(u)

                        self.write_to_file(self._teacher_file, teachers)
                        self.write_to_file(self._student_file, students)
                    else:
                        print("no find student.")
                else:
                    print("no find group.")
            else:
                print("no find teacher.")
        except Exception as e:
            print(e)
            self.subject_menu()

    # subject menu for
    def create_subject(self):
        students = self.read_to_file(self._student_file)
        teachers = self.read_to_file(self._teacher_file)
        try:
            teacher_list_user = []
            teacher_list_name = []
            for i, j in teachers.items():
                teacher_list_user.append(i)
                teacher_list_name.append(j["name"])
            if len(teacher_list_user) > 0:
                print('choice teacher')
                teacher_name = self.list_choice(teacher_list_name)
                teacher_user_index = teacher_list_name.index(teacher_name)
                teacher = teacher_list_user[teacher_user_index]
                group_list = []
                for i in teachers[teacher]["group"].keys():
                    group_list.append(i)
                if len(group_list) > 0:
                    print("choice group")
                    gr = self.list_choice(group_list)
                    direction_list = []
                    for i in teachers[teacher]["group"][gr].keys():
                        direction_list.append(i)
                    if len(direction_list) > 0:
                        print("choice direction")
                        direction = self.list_choice(direction_list)
                        count_list = []
                        for i in teachers[teacher]["group"][gr][direction].keys():
                            count_list.append(i)
                        subject_name = input("Subject name: ")
                        subject_time = input("Subject time(exp: 22.07.2024): ")

                        teachers[teacher]["group"][gr][direction][f"lesson_{len(count_list) + 1}"] = {
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
                                        teachers[teacher]["group"][gr][direction][f"lesson_{len(count_list) + 1}"][
                                            "students"].update(user)
                            self.write_to_file(self._teacher_file, teachers)
                            self.write_to_file(self._student_file, students)
                        else:
                            print("no find students")
                    else:
                        print("no find directions")
                else:
                    print("no found group")
            else:
                print("no find teacher")
        except Exception as e:
            print(e)
            self.show_menu_admin()

    # subject menu for
    def read_subject(self):
        teachers = self.read_to_file(self._teacher_file)
        try:
            teacher_list_user = []
            teacher_list_name = []
            for i, j in teachers.items():
                teacher_list_user.append(i)
                teacher_list_name.append(j["name"])
            if len(teacher_list_user) > 0:
                print('choice teacher')
                teacher_name = self.list_choice(teacher_list_name)
                teacher_user_index = teacher_list_name.index(teacher_name)
                teacher = teacher_list_user[teacher_user_index]
                group_list = []
                for i in teachers[teacher]["group"].keys():
                    group_list.append(i)
                if len(group_list) > 0:
                    print("choice group")
                    gr = self.list_choice(group_list)
                    direction_list = []
                    for i in teachers[teacher]["group"][gr].keys():
                        direction_list.append(i)
                    if len(direction_list) > 0:
                        print("choice direction")
                        direction = self.list_choice(direction_list)
                        for i, j in teachers[teacher]["group"][gr][direction].items():
                            text = f"""
        {i}:
            lesson time -> {j["lesson_time"]}
            lesson subject -> {j["lesson_name"]}
                        """
                            print(text)
                    else:
                        self.add_direction()
                        self.read_subject()
                else:
                    self.add_group()
                    self.read_subject()
            else:
                self.add_teacher()
                self.read_subject()
        except Exception as e:
            print(e)
            self.show_menu_admin()

    # subject menu for
    def update_subject(self):
        students = self.read_to_file(self._student_file)
        teachers = self.read_to_file(self._teacher_file)
        try:
            teacher_list_user = []
            teacher_list_name = []
            for i, j in teachers.items():
                teacher_list_user.append(i)
                teacher_list_name.append(j["name"])
            if len(teacher_list_user) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_list_name)
                teacher_user_index = teacher_list_name.index(teacher_name)
                teacher = teacher_list_user[teacher_user_index]
                group_list = []
                for i in teachers[teacher]["group"].keys():
                    group_list.append(i)
                if len(group_list) > 0:
                    print("choice group")
                    gr = self.list_choice(group_list)
                    direction_list = []
                    for i in teachers[teacher]["group"][gr].keys():
                        direction_list.append(i)
                    if len(direction_list) > 0:
                        print("choice direction")
                        direction = self.list_choice(direction_list)
                        lesson_list = []
                        for i in teachers[teacher]["group"][gr][direction].keys():
                            lesson_list.append(i)
                        if len(lesson_list) > 0:
                            print("choice direction")
                            lesson = self.list_choice(lesson_list)
                            subject_name = input("New subject name: ")
                            subject_time = input("New subject time(exp: 22.07.2024): ")
                            teachers[teacher]["group"][gr][direction][lesson]["lesson_time"] = subject_time
                            teachers[teacher]["group"][gr][direction][lesson]["lesson_name"] = subject_name
                            user_list = []
                            for i, j in students.items():
                                if j["group"] == gr:
                                    if direction in j["direction"].keys():
                                        user_list.append(i)
                            if len(user_list) > 0:
                                for i in user_list:
                                    students[i]["direction"][direction][lesson]["lesson_time"] = subject_time
                                    students[i]["direction"][direction][lesson]["lesson_name"] = subject_name
                                self.write_to_file(self._teacher_file, teachers)
                                self.write_to_file(self._student_file, students)
                            else:
                                self.add_student()
                                self.create_subject()
                        else:
                            self.create_subject()
                            self.update_subject()
                    else:
                        self.add_direction()
                        self.create_subject()
                else:
                    self.add_group()
                    self.create_subject()
            else:
                self.add_teacher()
                self.create_subject()
        except Exception as e:
            print(e)
            self.show_menu_admin()

    # subject menu for
    def delete_direction(self):
        students = self.read_to_file(self._student_file)
        teachers = self.read_to_file(self._teacher_file)
        try:
            teacher_list_user = []
            teacher_list_name = []
            for i, j in teachers.items():
                teacher_list_user.append(i)
                teacher_list_name.append(j["name"])
            if len(teacher_list_user) > 0:
                print('choice teacher')
                teacher_name = self.list_choice(teacher_list_name)
                teacher_user_index = teacher_list_name.index(teacher_name)
                teacher = teacher_list_user[teacher_user_index]
                group_list = []
                for i in teachers[teacher]["group"].keys():
                    group_list.append(i)
                if len(group_list) > 0:
                    print("choice group")
                    gr = self.list_choice(group_list)
                    direction_list = []
                    for i in teachers[teacher]['group'][gr].keys():
                        direction_list.append(i)
                    print('choice direction')
                    if len(direction_list) > 0:
                        direction = self.list_choice(direction_list)
                        del teachers[teacher]["group"][gr][direction]
                        user_list = []
                        for i, j in students.items():
                            if j["group"] == gr:
                                if direction in j["direction"].keys():
                                    user_list.append(i)
                        if len(user_list) > 0:
                            for i in user_list:
                                del students[i]["direction"][direction]
                            self.write_to_file(self._teacher_file, teachers)
                            self.write_to_file(self._student_file, students)
                        else:
                            print("no choice direction")
                            self.subject_menu()
                    else:
                        print("no choice direction")
                        self.subject_menu()
                else:
                    print("no choice direction")
                    self.subject_menu()
            else:
                print("no choice direction")
                self.subject_menu()
        except Exception as e:
            print(e)

    def teacher_menu(self):
        text = """
        1. Add teacher
        2. Delete teacher
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.add_teacher()
        elif num == 2:
            self.delete_teacher()
        else:
            return

    # teacher menu for
    def add_teacher(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name = input("Enter teacher name: ").title()
        phone = self.phone_input("Enter teacher phone number: ")
        num = random.randint(100000, 999999)
        while f"TM{num}" == teachers.keys():
            num = random.randint(100000, 999999)
        parol = random.randint(1000000, 9999999)
        p = hashlib.sha256(str(parol).encode()).hexdigest()
        for i in teachers.values():
            while parol == i["password"]:
                parol = random.randint(1000000, 9999999)
                p = hashlib.sha256(str(parol).encode()).hexdigest()
        user = {
            f"TM{num}": {
                "name": teacher_name,
                "phone_number": phone,
                "password": p,
                "group": {}
            }
        }
        teachers.update(user)
        self.write_to_file(self._teacher_file, teachers)
        print(f"teacher username:{f"TM{num}"}, password:{parol}")

    # teacher menu for
    def delete_teacher(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                del teachers[teacher]
                self.write_to_file(self._teacher_file, teachers)
            else:
                print("no choice teacher")
        except KeyError:
            print("no choice teacher")

    def group_menu(self):
        text = """
        1. Add group
        2. Delete group
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.add_group()
        elif num == 2:
            self.delete_group()
        else:
            return

    # group_name for
    def add_group(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                group_name = input("group name: ")
                gr = {group_name: {}}
                teachers[teacher]["group"].update(gr)
                self.write_to_file(self._teacher_file, teachers)
            else:
                print("no choice teacher.")
        except KeyError:
            print("no choice teacher.")

    # group_name for
    def delete_group(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                gr_list = []
                for i in teachers[teacher]["group"].keys():
                    gr_list.append(i)
                print("choice group")
                gr = self.list_choice(gr_list)
                del teachers[teacher]["group"][gr]
                self.write_to_file(self._teacher_file, teachers)
            else:
                print("no choice teacher.")
        except KeyError:
            print("no choice teacher.")

    def student_menu(self):
        text = """
        1. Add student
        2. Delete student
        3. Exit
        """
        print(text)
        num = int_input('number: ')
        if num == 1:
            self.add_student()
        elif num == 2:
            self.delete_student()
        else:
            return

    # student menu for
    def add_student(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                gr_list = []
                for i in teachers[teacher]["group"].keys():
                    gr_list.append(i)
                print("choice group")
                gr = self.list_choice(gr_list)
                direction_list = []
                for i in teachers[teacher]["group"][gr].keys():
                    direction_list.append(i)
                direction = self.list_choice(direction_list)
                students: dict = self.read_to_file(self._student_file)
                name = input("Enter student name:").title()
                num = random.randint(100000, 999999)
                while f"SP{num}" == students.keys():
                    num = random.randint(100000, 999999)
                parol = random.randint(1000000, 9999999)
                p = hashlib.sha256(str(parol).encode()).hexdigest()
                for i in students.values():
                    while i["password"] == p:
                        parol = random.randint(1000000, 9999999)
                        p = hashlib.sha256(str(parol).encode()).hexdigest()
                user = {
                    f"SP{num}": {
                        "password": p,
                        "student_name": name,
                        "group": gr,
                        "teacher": teachers[teacher]["name"],
                        "direction": {direction: {}}
                    }
                }
                students.update(user)
                username = f"SP{num}"
                self.write_to_file(self._student_file, students)
                print(f"username: {username}, password: {parol}")
            else:
                print("no find teacher")
        except KeyError:
            print("no find teacher")

    # student menu for
    def delete_student(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                gr_list = []
                for i in teachers[teacher]["group"].keys():
                    gr_list.append(i)
                print("choice group")
                gr = self.list_choice(gr_list)
                students: dict = self.read_to_file(self._student_file)
                student_user = []
                student_name = []
                for i, j in students.items():
                    if j["group"] == gr:
                        student_user.append(i)
                        student_name.append(j["student_name"])
                n = self.list_choice(student_name)
                s_index = student_name.index(n)
                student = student_user[s_index]
                del students[student]
                self.write_to_file(self._student_file, students)
            else:
                print("no find teacher.")
        except KeyError:
            print("no find teacher.")

    def manage_lessons(self):
        teachers: dict = self.read_to_file(self._teacher_file)
        teacher_name_list = []
        teacher_user_list = []
        try:
            for i, j in teachers.items():
                teacher_user_list.append(i)
                teacher_name_list.append(j["name"])
            if len(teacher_user_list) > 0:
                print("choice teacher")
                teacher_name = self.list_choice(teacher_name_list)
                t_index = teacher_name_list.index(teacher_name)
                teacher = teacher_user_list[t_index]
                gr_list = []
                for i in teachers[teacher]["group"].keys():
                    gr_list.append(i)
                if len(gr_list) > 0:
                    print("choice group")
                    gr = self.list_choice(gr_list)
                    direction_list = []
                    for i in teachers[teacher]["group"][gr].keys():
                        direction_list.append(i)
                    if len(direction_list) > 0:
                        print("choice direction")
                        direction = self.list_choice(direction_list)
                        lesson_list = []
                        for i in teachers[teacher]["group"][gr][direction].keys():
                            lesson_list.append(i)
                        if len(lesson_list) > 0:
                            lesson = self.list_choice(lesson_list)
                            print("lesson subject: ", end="")
                            print(teachers[teacher]["group"][gr][direction][lesson]["lesson_name"])
                            print("lesson time: ", end="")
                            print(teachers[teacher]["group"][gr][direction][lesson]["lesson_time"])
                        else:
                            print("no find lessons")
                    else:
                        print("no find direction")
                else:
                    print("no find group")
            else:
                print("no find teacher.")
        except KeyError:
            print("no find teacher.")


d = Admin()
d.show_menu_admin()
