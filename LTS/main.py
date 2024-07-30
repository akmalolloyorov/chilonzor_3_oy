from LTS.superadmin.super_admin import SuperAdmin, int_input
from LTS.Extra.about import about
import hashlib


class Main(SuperAdmin):

    def show_menu(self):

        text = """
        1. Login
        2. About the Website
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.login()
        elif num == 2:
            about()
            self.show_menu()
        else:
            print("Goodbye!")

    def login(self):
        student_file: dict = self.read_to_file(self._student_file)
        admin_file: dict = self.read_to_file(self._admin_file)
        super_admin_file: dict = self.read_to_file(self._super_admin)
        teacher_file: dict = self.read_to_file(self._teacher_file)
        username: str = input("Username: ")
        parol: str = input("Password: ")
        p: str = hashlib.sha256(parol.encode()).hexdigest()
        if "AAA" in username:  # super Admin
            if super_admin_file[username]["password"] == p:
                while self.show_menu_super_admin(teacher_file, student_file, admin_file) == 'num':
                    return self.show_menu()
            else:
                print("Wrong input")
                self.login()
        elif "AS" in username:  # Admin
            if admin_file[username]["password"] == p:
                while self.show_menu_admin(teacher_file=teacher_file, student_file=student_file) == "num":
                    return self.show_menu()
            else:
                print("Wrong input")
                self.login()
        elif "TM" in username:  # Teacher
            if teacher_file[username]["password"] == p:
                while self.show_menu_teacher(username=username, teacher_file=teacher_file) == "num":
                    return self.show_menu()
            else:
                print("Wrong input")
                self.login()
        elif "SP" in username:  # Student
            if student_file[username]["password"] == p:
                while self.show_menu_student(username=username, student_file=student_file) == "num":
                    return self.show_menu()
            else:
                print("Wrong input")
                self.login()
        else:
            print("Wrong input...")
            self.show_menu()


m = Main()
try:
    m.show_menu()
except KeyboardInterrupt:
    pass

"""
Admin, Teacher, Student,Super admin lar kerak bo'lsa fayllarda 
o'zlari uchun addelni fayylar ochilgan birinchi keyi 
username boshida ikkita harf bilan yozilgan, 
parol esa hammasining paroli '5' ga teng  username va parol bilan birgalikda login qilasiz"""

"""
brinchi bo'lib Teacher qo'shiladi
ikkinchi bo'lib group qo'shiladi
uchinchi bo'lib Direction qo'shiladi
to'rtinchi bo'lib Student qo'shiladi
aytmoqchi bo'lganim student qo'shmoqchi bo'lsagiz direction bo'lishi kerak
direction qo'shmoqchi bo'lsanigiz group bo'lishi kerak 
group qo'shmoqchi bo'lsanigiz teacher bo'llishi kerak
"""

""" 
Super admin qismi code hali yozilmagan
"""
