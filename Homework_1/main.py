""" N50gram -> Chat yasash kerak: Registeratsiya bo'lishi kerak,
username va parol bilan Login ham bo'lishi kerak Auth

menu: - Register | full_name, username, password
      - Login | username, password
      - Exit

Menu: - Create chat | chat_code -> chat random id
      - Join the chat | -> chat_id, chat_code
      - Delete chat | chat_id
      - Show my created chats
      - Show my joined chats
      - Exit

Chat menu: - Send message
           - Show all message
           - Exit
terminalni o'chirib qaytib kirsam, chatni malumotlari o'chib ketsa ham bo'ladi """
from user import User, int_input
import hashlib


class Main(User):
    def show_menu(self):
        text = """
        1. Register | fullname, username, password
        2. Login | username, password
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.register()
        elif num == 2:
            self.login()
        else:
            print("The end...")

    def register(self):
        full_name = input("Fullname: ").title()
        username = input("username: ")
        parol = input("Password: ")
        p = hashlib.sha256(parol.encode()).hexdigest()
        user = {
            username: {
                "full_name": full_name,
                "password": p,
                "my_joined": []
            }
        }
        self.add_to_file(self._user_file, user)
        if self.show_menu_user(username) == 6:
            return self.show_menu()

    def login(self):
        username = input("Username: ")
        parol = input("Password: ")
        p = hashlib.sha256(parol.encode()).hexdigest()
        user: dict = self.read_to_file(self._user_file)
        count = 3
        while count > 0:
            if user[username]["password"] == p:
                if self.show_menu_user(username) == 6:
                    return self.show_menu()
            else:
                print("Wrong input...")
                count -= 1


main = Main()
try:
    main.show_menu()
except KeyboardInterrupt:
    pass
