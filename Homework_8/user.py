from Json_manager import JsonManager, int_input
import json


class User(JsonManager):
    def show_menu_user(self, gmail: str):
        text = """
        1. show all new messages
        2. show all read messages
        3. Logout
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.show_all_new_messages(gmail)
            self.show_menu_user(gmail)
        elif num == 2:
            self.show_all_read_messages(gmail)
            self.show_menu_user(gmail)
        else:
            self.active = True
            return self.active

    def show_all_new_messages(self, gmail):
        user_file: dict = self.read_to_file(self.users_file)
        sms_list = []
        a_list = []
        for i in user_file[gmail]['messages']:
            for j, k in i.items():
                a_list.append(j)
                if not k['is_read']:
                    sms_list.append(j)
        if len(sms_list) > 0:
            sms = self.list_choice(sms_list)
            index = a_list.index(sms)
            print(f"massage:{user_file[gmail]['messages'][index][sms]['massage']}")
            print(f"time: {user_file[gmail]['messages'][index][sms]['time']}")
            user_file[gmail]['messages'][index][sms]['is_read'] = True
            self.write_to_file(self.users_file, user_file)
        else:
            print("No new messages")

    def show_all_read_messages(self, gmail):
        user_file: dict = self.read_to_file(self.users_file)
        sms_list = []
        a_list = []
        for i in user_file[gmail]['messages']:
            for j, k in i.items():
                a_list.append(j)
                if k['is_read']:
                    sms_list.append(j)
        if len(sms_list) > 0:
            sms = self.list_choice(sms_list)
            index = a_list.index(sms)
            print(f"massage:{user_file[gmail]['messages'][index][sms]['massage']}")
            print(f"time: {user_file[gmail]['messages'][index][sms]['time']}")
            self.write_to_file(self.users_file, user_file)
        else:
            print("No new messages")


def read_keys_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for key in data.keys():
            yield key


u = User()


def generatr_for():
    gmail_list = []
    for key in read_keys_from_file(u.users_file):
        gmail_list.append(key)
    return gmail_list
