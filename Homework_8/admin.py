from user import User, int_input, generatr_for
import smtplib
import threading

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_sender = "sanjarbekwork@gmail.com"
smtp_password = 'nlcg jpcd umyu zcog'


def send_mail(to_user, subject, massage):
    email = f"Subject: {subject}\n\n{massage}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")


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
            self.show_menu_admin()
        elif num == 2:
            self.send_massage_from_gmail()
        elif num == 3:
            self.show_sent_message_with_time()
            self.show_menu_admin()
        else:
            self.active = True
            return True

    def show_all_users(self):
        users_file: dict = self.read_to_file(self.users_file)
        users_list = generatr_for()
        if len(users_list) > 0:
            for i in users_list:
                text = f"""
        Full name: {users_file[i]["full_name"]}
          email: {i}
          gender: {users_file[i]["gender"]}
          age: {users_file[i]["age"]}
                       """
                print(text)
        else:
            print("no find users...")

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
            self.to_all_users()
            self.send_massage_from_gmail()
        elif num == 2:
            self.to_males()
            self.send_massage_from_gmail()
        elif num == 3:
            self.to_females()
            self.send_massage_from_gmail()
        elif num == 4:
            self.higher_from_18()
            self.send_massage_from_gmail()
        elif num == 5:
            self.lower_from_18()
            self.send_massage_from_gmail()
        else:
            self.show_menu_admin()

    def to_all_users(self):
        users_file = self.read_to_file(self.users_file)
        subject = input('Subject: ')
        massage = input('Massage: ')
        user_list = generatr_for()
        if len(user_list) > 0:
            for i in users_file:
                t = threading.Thread(target=send_mail, args=(i, subject, massage))
                t.start()
                sms = {subject: {
                    "time": self.current_time(),
                    "massage": massage,
                    "is_read": False
                }}
                users_file[i]["messages"].append(sms)
                self.write_to_file(self.users_file, users_file)
            print('massage sent successfully')
        else:
            print("no choice users")

    def to_males(self):
        users_file: dict = self.read_to_file(self.users_file)
        subject = input('Subject: ')
        massage = input('Massage: ')
        users_list = generatr_for()
        gender_list = []
        for i in users_list:
            for j in users_file[i]['gender']:
                if j == "male":
                    gender_list.append(i)
        if len(gender_list) > 0:
            for i in gender_list:
                t = threading.Thread(target=send_mail, args=(i, subject, massage))
                t.start()
                sms = {subject: {
                    "time": self.current_time(),
                    "massage": massage,
                    "is_read": False
                }}
                users_file[i]["messages"].append(sms)
                self.write_to_file(self.users_file, users_file)
            print('massage sent successfully')
        else:
            print("no choice users")

    def to_females(self):
        users_file: dict = self.read_to_file(self.users_file)
        subject = input('Subject: ')
        massage = input('Massage: ')
        users_list = generatr_for()
        gender_list = []
        for i in users_list:
            for j in users_file[i]['gender']:
                if j == "female":
                    gender_list.append(i)
        if len(gender_list) > 0:
            for i in gender_list:
                t = threading.Thread(target=send_mail, args=(i, subject, massage))
                t.start()
                sms = {subject: {
                    "time": self.current_time(),
                    "massage": massage,
                    "is_read": False
                }}
                users_file[i]["messages"].append(sms)
                self.write_to_file(self.users_file, users_file)
            print('massage sent successfully')
        else:
            print("no choice users")

    def higher_from_18(self):
        users_file: dict = self.read_to_file(self.users_file)
        subject = input('Subject: ')
        massage = input('Massage: ')
        users_list = generatr_for()
        age_list = []
        for i in users_list:
            for j in users_file[i]['age']:
                if j >= 18:
                    age_list.append(i)
        if len(age_list) > 0:
            for i in age_list:
                t = threading.Thread(target=send_mail, args=(i, subject, massage))
                t.start()
                sms = {subject: {
                    "time": self.current_time(),
                    "massage": massage,
                    "is_read": False
                }}
                users_file[i]["messages"].append(sms)
                self.write_to_file(self.users_file, users_file)
            print('massage sent successfully')
        else:
            print("no choice users")

    def lower_from_18(self):
        users_file: dict = self.read_to_file(self.users_file)
        subject = input('Subject: ')
        massage = input('Massage: ')
        users_list = generatr_for()
        age_list = []
        for i in users_list:
            for j in users_file[i]['age']:
                if j < 18:
                    age_list.append(i)
        if len(age_list) > 0:
            for i in age_list:
                t = threading.Thread(target=send_mail, args=(i, subject, massage))
                t.start()
                sms = {subject: {
                    "time": self.current_time(),
                    "massage": massage,
                    "is_read": False
                }}
                users_file[i]["messages"].append(sms)
                self.write_to_file(self.users_file, users_file)
            print('massage sent successfully')
        else:
            print("no choice users")

    def show_sent_message_with_time(self):
        users_file = self.read_to_file(self.users_file)
        users_list = generatr_for()
        if len(users_list) > 0:
            for i in users_list:
                for j in users_file[i]['messages']:
                    for k, l in j.items():
                        print(f"Full name- {users_file[i]["full_name"]},  massage-{l['massage']}, time-{l['time']}")
        else:
            print("no choice users")


a = Admin()
a.show_sent_message_with_time()
