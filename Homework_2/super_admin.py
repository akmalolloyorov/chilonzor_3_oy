from admin import Admin


class SuperAdmin(Admin):
    def show_menu_super_admin(self):
        print("COMING SOON")
        self.__str__()
        return 0
