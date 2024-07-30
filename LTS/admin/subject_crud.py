from LTS.admin.student_crud import StudentCrud, int_input


class SubjectCurd(StudentCrud):
    def subject_crud(self, teacher_file: dict, student_file: dict) -> str:
        text = """
        1. Add direction
        2. Add lesson
        3. Delete direction
        4. Change Lesson Topic
        5. View directions
        6. View lessons
        """
        print(text)
        num = int_input("Number: ")
        if num == 1:
            self.add_direction(teacher_file=teacher_file, student_file=student_file)
        elif num == 2:
            self.add_lesson(teacher_file=teacher_file, student_file=student_file)
        elif num == 3:
            self.delete_direction(teacher_file=teacher_file, student_file=student_file)
        elif num == 4:
            self.change_lesson_topic_t(teacher_file=teacher_file, student_file=student_file)
        elif num == 5:
            self.view_directions(teacher_file=teacher_file)
        elif num == 6:
            self.view_lessons_teacher(teacher_file=teacher_file, student_file=student_file)
        else:
            return 'num'
        self.delete_direction(teacher_file=teacher_file, student_file=student_file)

    def add_direction(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher"]
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher = my_list[0]
        new_direction: str = input("Enter new direction: ")
        teacher_file[teacher]["direction"][new_direction] = {}
        self.write_to_file(self._teacher_file, teacher_file)

    def add_lesson(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher"]
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher = my_list[0]
        self.add_new_lesson(username=teacher, teacher_file=teacher_file)

    def delete_direction(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher", 'direction']
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher = my_list[0]
        direction: str = my_list[1]
        del teacher_file[teacher][direction]
        self.write_to_file(self._teacher_file, teacher_file)

    def change_lesson_topic_t(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher"]
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher = my_list[0]
        self.change_lesson_topic(username=teacher, teacher_file=teacher_file)

    def view_directions(self, teacher_file: dict) -> None:
        self.__str__()
        for teacher, teacher_value in teacher_file.items():
            for direction in teacher_value['direction'].keys():
                print(f"Teacher: {teacher}, Direction: {direction}")

    def view_lessons_teacher(self, teacher_file: dict, student_file: dict) -> None:
        for_list: list = ["teacher"]
        my_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, for_list)
        teacher = my_list[0]
        self.view_lessons(username=teacher, teacher_file=teacher_file)
