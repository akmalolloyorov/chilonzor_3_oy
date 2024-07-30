"""
Hemis ga o'xshagan sistema yasash kerak,
bu vazifada faqatgina admin qismini qilib kelish kerak holos
     Users: 1.
     Admin 2.
     Teacher 3.
Student Auth Menu:
     1. Login
     2. Exit

Teacher menu:
     1. Show my active lessons
     2. Start lesson: -> lesson_id - Grading -> student_id, grade - End lesson
     3. Show my ended lessons
     4. Logout
Student menu:
     1. Show my active lessons
     2. Show my grade
     3. Show my grade by subject
     4. Logout
"""
from student import Student
from super_admin import SuperAdmin
import hashlib


class Main(Student, SuperAdmin):

    def show_menu(self):
        student_file: dict = self.read_to_file(self._student_file)
        admin_file: dict = self.read_to_file(self._admin_file)
        super_admin_file: dict = self.read_to_file(self._super_admin)
        teacher_file: dict = self.read_to_file(self._teacher_file)
        print("             Login")
        username = input("Username: ")
        parol = input("Password: ")
        p = hashlib.sha256(parol.encode()).hexdigest()
        if "AAA" in username:  # super Admin
            if super_admin_file[username]["password"] == p:
                if self.show_menu_super_admin() == 0:
                    self.show_menu()
            else:
                print("Wrong input")
        elif "AS" in username:  # Admin
            if admin_file[username]["password"] == p:
                if self.show_menu_admin() == 0:
                    self.show_menu()
            else:
                print("Wrong input")
        elif "TM" in username:  # Teacher
            if teacher_file[username]["password"] == p:
                if self.show_menu_teacher(username) == 0:
                    self.show_menu()
            else:
                print("Wrong input")
        elif "SP" in username:  # Student
            if student_file[username]["password"] == p:
                if self.show_menu_student(username) == 0:
                    self.show_menu()
            else:
                print("Wrong input")
        else:
            print("Wrong input...")


m = Main()
try:
    m.show_menu()
except KeyboardInterrupt:
    pass
