from user import User, int_input

"""
Admin menu:
    - show all users | if you use generator to print users data (ijson)
    - send message from gmail:
        0. To all users
        1. To males
        2. To females
        3. Higher from 18
        4. Lower from 18
    - show sent message with time
    - Logout"""


class Admin(User):
    def show_menu_admin(self):
        text = """
        1. show all users | if you use generator to print users data ()
        2. send message from gmail:
        3. show sent message with time
        4. Logout
        """
        print(text)
        num = int_input('number: ')
        if num == 1:
            self.show_all_users()
        elif num == 2:
            self.send_massage_from_gmail()
        elif num == 3:
            self.show_sent_message_with_time()
        else:
            self.active = True
            return True

    def show_all_users(self):
        pass

    def send_massage_from_gmail(self):
        text = """
         1. To all users
         2. To males
         3. To females
         4. Higher from 18
         5. Lower from 18
         6. Exit
        """
        print(text)
        num = int_input('number: ')
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        else:
            self.show_menu_admin()

    def show_sent_message_with_time(self):
        pass
