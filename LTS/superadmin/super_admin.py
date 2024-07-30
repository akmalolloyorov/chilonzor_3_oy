from LTS.admin.admin import Admin, int_input
import hashlib
import random


class SuperAdmin(Admin):
    def show_menu_super_admin(self, teacher_file: dict, student_file: dict, admin_file: dict) -> str:
        text = """
        1. Add admin
        2. delete admin
        3. change admin
        4. others
        """
        print(text)
        num = int_input('number: ')
        if num == 1:
            self.add_admin(admin_file=admin_file)
        elif num == 2:
            self.delete_admin(admin_file=admin_file)
        elif num == 3:
            self.change_admin_info(admin_file=admin_file)
        elif num == 4:
            self.other_operations(teacher_file=teacher_file, student_file=student_file)
        else:
            return "num"

    def add_admin(self, admin_file: dict) -> None:
        num: int = random.randint(100000, 999999)
        while f"TM{num}" in admin_file.keys():
            num: int = random.randint(100000, 999999)
        username = f"TM{num}"
        parol: int = random.randint(1000000, 9999999)
        while parol in admin_file.values():
            parol: int = random.randint(1000000, 9999999)
        p: str = hashlib.sha256(str(parol).encode()).hexdigest()
        admin_name = input("Admin name: ").title()
        admin_phone = self.phone_input("Enter admin phone number: ")
        user: dict = {
            username: {
                "password": p,
                "admin_name": admin_name,
                "phone_number": admin_phone
            }
        }
        self.add_to_file(self._admin_file, user)

    def delete_admin(self, admin_file: dict) -> None:
        admin_name_list: list = []
        admin_user_list: list = []
        for admin, admin_value in admin_file.items():
            for admin_name in admin_value["admin_name"]:
                admin_name_list.append(admin_name)
                admin_user_list.append(admin)
        admin_name = self.list_choice(admin_name_list)
        admin_index = admin_name_list.index(admin_name)
        admin_user = admin_user_list[admin_index]
        del admin_file[admin_user]
        self.write_to_file(self._admin_file, admin_file)

    def change_admin_info(self, admin_file: dict) -> None:
        admin_name_list: list = []
        admin_user_list: list = []
        for admin, admin_value in admin_file.items():
            for admin_name in admin_value["admin_name"]:
                admin_name_list.append(admin_name)
                admin_user_list.append(admin)
        admin_name = self.list_choice(admin_name_list)
        admin_index = admin_name_list.index(admin_name)
        admin_user = admin_user_list[admin_index]
        admin_name = input("Enter admin name").title()
        admin_password = input("new password: ")
        p: str = hashlib.sha256(str(admin_password).encode()).hexdigest()
        admin_phone = self.phone_input("admin phone: ")
        admin_file[admin_user]['admin_name'] = admin_name
        admin_file[admin_user]['password'] = p
        admin_file[admin_user]['phone_number'] = admin_phone
        self.write_to_file(self._admin_file, admin_file)

    def other_operations(self, teacher_file: dict, student_file: dict) -> None:
        self.show_menu_admin(teacher_file=teacher_file, student_file=student_file)
