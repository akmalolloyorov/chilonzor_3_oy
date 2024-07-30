""" Aviachiptalarni sotib olish uchun dastur tuzish kerak.
Har bitta operatsiyani log faylga yozib borish kerak.
Try exceptlardan foydalaning

Auth menu:
- Login
- Register
- Exit

Admin:
- Add plane (CRUD): id, name, capacity
- Add airport (CRUD): name, country
- Add flight: plane, from_airport, to_airport, flight_time, landing_time, status, tickets=0, price
- Show all flights:
- Logout

User:
- Search flights: from_airport, to_airport -> all the available flights:
- Buy ticket - Passport number, gmail
- Back
- My booked flights:
- Logout """
from admin import Admin, int_input
import hashlib


class Main(Admin):
    def show_menu(self):
        text = """
        1. Log in 
        2. Register
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.login()
        elif num == 2:
            self.register()
        elif num == self._admin_password:
            self.show_menu_admin()
            if self.exit:
                self.show_menu()
                self.exit = False
        else:
            print("The end...")

    def login(self):
        if self._is_active:
            self.show_menu_user(self._active_phone)
            if self.exit:
                self.show_menu()
                self.exit = False
        else:
            print("Type exit to leave")
            phone = self.phone_input("Enter phone number: ")
            if phone != "exit":
                print("Type exit to leave")
                parol = input("Enter password: ")
                if phone != 'exit':
                    p = hashlib.sha256(parol.encode("utf-8")).hexdigest()
                    user_file = self.read_to_file(self._user_file)
                    if user_file[f"+998{phone}"]["password"] == p:
                        self.show_menu_user(phone_number=phone)
                        if self.exit:
                            self.show_menu()
                            self.exit = False
                            self._active_phone = f"+998{phone}"
                    else:
                        print("Wrong phone number or password!")
                        self.login()
                else:
                    self.show_menu()
            else:
                self.show_menu()

    def register(self):
        phone = self.phone_input("Phone number (exp - 972203565): ")
        parol1 = input("Enter password: ")
        parol2 = input("Enter your password again    : ")
        if parol2 == parol1:
            p = hashlib.sha256(str(parol1).encode("utf-8")).hexdigest()
            user = {
                f"998{phone}": {
                    "password": p,
                    "purchased_tickets": {},
                }
            }
            self.add_to_file(self._user_file, user)
            self._is_active = True
            print("Registration completed successfully!")
            self.show_menu()
        else:
            print("Passwords don't match!")
            self.register()


main = Main()
if __name__ == '__main__':
    main.show_menu()
