from LTS.admin.teacher_crud import TeacherCrud, int_input


class Admin(TeacherCrud):
    def show_menu_admin(self, teacher_file: dict, student_file: dict) -> str:
        text = """
        1. Teacher CRUD
        2. Group CRUD
        3. Student CRUD
        4. Subject CRUD
        5. Logout
        """
        print(text)
        num = int_input("Number: ")
        if num == 1:
            while self.teacher_crud(teacher_file=teacher_file, student_file=student_file) == "num":
                return self.show_menu_admin(teacher_file, student_file)
        elif num == 2:
            while self.group_crud(teacher_file=teacher_file, student_file=student_file) == "num":
                return self.show_menu_admin(teacher_file, student_file)
        elif num == 4:
            while self.subject_crud(teacher_file=teacher_file, student_file=student_file) == "num":
                return self.show_menu_admin(teacher_file, student_file)
        elif num == 3:
            while self.student_crud(teacher_file=teacher_file, student_file=student_file) == "num":
                return self.show_menu_admin(teacher_file, student_file)
        else:
            return "num"
