"""
Tasavvur qiling Najot Ta'limda yangiliklarni email orqali olish imkoni
paydo bo'ldi. Ya'ni qandaydir yangilik bo'lsa sizga kiritgan email
akauntingiz uchun habar kelib turadi.

Sizni vazifangiz shunga o'xshash dastur yaratish. Ya'ni men dasturni ishga tushurganimda u menda
login, register so'raydi. Ro'yxatdan o'tish uchun men email akauntimni kiritaman va tasdiqlayman.
Va menga kelgan habarlarni ko'rib turishim mumkin bo'ladi.

Agar admin bo'lsam menda hamma foydalanuvchilarni ko'rish, va ularga gmail orqali
habar yuborish imkoni bo'lishi kerak. Habarlarni ushbu kategorilar orqali yuborishim
mumkin:
0. Hamma uchun
1. Faqat qizlar uchun habar
2. Faqat yigitlar uchun habar
3. 18 yoshdan kattalar uchun
4. 18 yoshdan kichiklar uchun

Foydalanuvchi ro'yxatdan o'tayotgan vaqtida ismini, yoshini, jinsini, gmail, parol malumotlarini kiritadi.


Auth menu:
    - Register
        - gmail, password, confirm_password, full_name, age, gender
    - Login
        - gmail, password
    - Exit




"""
import hashlib

from admin import Admin, int_input, send_mail
import random
import threading


class Main(Admin):
    def __init__(self):
        super().__init__()
        self.confirm_password = None

    def random_num(self):
        num = random.randint(100000, 999999)
        self.confirm_password = num
        return num

    def show_menu(self):
        text = """
        Pass authentication
        1.Register | gmail, password, confirm_password, full_name, age, gender
        2.Login | gmail, password
        3.Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.register()
        elif num == 2:
            self.login()
        elif num == self.admin_password:
            self.show_menu_admin()
            if self.active:
                self.active = False
                self.show_menu()
        else:
            print("Goodbye...")

    def register(self):
        gmail = input("Enter your gmail address (exp:akmal@gmail.com): ").lower().strip()
        while "@gmail.com" not in gmail:
            gmail = input("Enter your gmail address (exp:akmal@gmail.com): ").lower().strip()
        parol = input("password: ")
        p = hashlib.sha256(parol.encode('utf8')).hexdigest()
        t = threading.Thread(target=send_mail, args=(gmail, f"confirm code: {self.random_num()}", "Please enter"))
        t.start()
        print("A confirmation code has been sent to you. Please enter the code.")
        confirm_password = int_input("Confirm password: ")
        if confirm_password == self.confirm_password:
            full_name = input("Full name: ").title()
            gender = input("Gender: ")
            age = int_input("Age: ")
            user = {
                gmail: {
                    "password": p,
                    "full_name": full_name,
                    "gender": gender,
                    "age": age,
                    "messages": [],
                    "is_active": False,
                    "read_messages": []
                }
            }
            self.add_to_file(self.users_file, user)
        else:
            print("Wrong input password.")
            self.show_menu()

    def login(self):
        users_file: dict = self.read_to_file(self.users_file)
        gmail = input("Gmail: ").lower().strip()
        parol = input("Password: ")
        p = hashlib.sha256(parol.encode('utf8')).hexdigest()
        if users_file[gmail]["password"] == p:
            users_file[gmail]["is_active"] = True
            self.show_menu_user(gmail=gmail)
            if self.active:
                self.active = False
                return self.show_menu()
            self.write_to_file(self.users_file, users_file)
        else:
            print("Wrong gmail or password.")
            self.show_menu()


main = Main()
main.show_menu()
