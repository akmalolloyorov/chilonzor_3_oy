from LTS.teacher.teacher import Teacher, int_input


class ForAdmin(Teacher):
    def for_admin_teacher_direction_lesson(self, teacher_file: dict, student_file: dict, my_list: list) -> str or int:
        a = 'no'
        if "teacher" in my_list:
            a = 't'
        if "teacher" and "direction" in my_list:
            a = 'td'
        if "teacher" and "direction" and 'lesson' in my_list:
            a = "tl"
        if "teacher" and "direction" and 'lesson' and 'user' in my_list:
            a = "tu"
        teacher_name_list = []
        teacher_list = []
        if len(teacher_file) > 0:
            for teacher, value in teacher_file.items():
                teacher_list.append(teacher)
                teacher_name_list.append(value['name'])
            teacher_name: str = self.list_choice(teacher_name_list)
            n_index = teacher_name_list.index(teacher_name)
            teacher = teacher_list[n_index]
            if a == "t":
                return [teacher]
            direction_list: list = []
            if len(teacher_file[teacher]['direction']) > 0:
                for direction in teacher_file[teacher]['direction'].keys():
                    direction_list.append(direction)
                direction = self.list_choice(direction_list)
                if a == "td":
                    return [teacher, direction]
                lesson_list: list = []
                if len(teacher_file[teacher]['direction'][direction]) > 0:
                    for lesson in teacher_file[teacher]['direction'][direction].keys():
                        lesson_list.append(lesson)
                    lesson = self.list_choice(lesson_list)
                    if a == "tl":
                        return [teacher, direction, lesson]
                    user_name_list: list = []
                    user_list: list = []
                    if len(teacher_file[teacher]['direction'][direction][lesson]['students']) > 0:
                        for user in teacher_file[teacher]['direction'][direction][lesson]['students'].keys():
                            user_list.append(user)
                            user_name_list.append(f"{student_file[user]['student_name']}")
                        user_name = self.list_choice(user_name_list)
                        m_index = user_name_list.index(user_name)
                        user = user_list[m_index]
                        if a == "tu":
                            return [teacher, direction, lesson, user]
                    else:
                        print("No user in this group!")
                        return ["user"]
                else:
                    print("No lesson in this direction!")
                    return ['lesson']
            else:
                print("No teacher's direction!")
                return ["direction"]
        else:
            print("No teacher!")
            return ["teacher"]

    def none(self):
        n = int_input(self.__str__())
        print(n)
