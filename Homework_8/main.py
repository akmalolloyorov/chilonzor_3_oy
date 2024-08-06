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




User menu:
    - show all new messages
    - show all read messages
    - Logout
"""

from admin import Admin, int_input


class Main(Admin):
    def __init__(self):
        super().__init__()
        self.is_active = False

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
        else:
            print("The end...")

    def register(self):
        gmail = input("Enter your gmail address (exp:akmal@gmail.com)").lower().strip()
        password = input("password: ")
        print("send sms email")
        confirm_password = input("Confirm password: ")
        full_name = input("Full name: ")
        gender = input("Gender: ")
        age = int(input("Age: "))
        user = {
            gmail: {
                "password": password,
                "full_name": full_name,
                "gender": gender,
                "age": age,
                "messages": [],
                "is_active": True,
                "read_messages": []
            }
        }
        self.add_to_file(self._users_file, user)

    def login(self):
        pass
