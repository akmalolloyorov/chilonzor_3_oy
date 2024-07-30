import json

from json_manager import JsonManager, int_input
import datetime


class Chats(JsonManager):
    def show_menu_chats(self, chat_id, username):
        text = """
        1. Send massage
        2. Show all massage
        3. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.send_massages(chat_id, username)
        elif num == 2:
            self.show_all_massages(chat_id, username)
        else:
            return 3

    def send_massages(self, chats_id: int, username: str):
        chats: dict = self.read_to_file(self._chats)
        if len(chats[chats_id]['massages']) > 0:
            print(json.dumps(chats[chats_id]['massages'], indent=4))
        now_time = datetime.datetime.now()
        chass_and_minute = now_time.strftime("%H:%M")
        date = now_time.strftime("%d-%m-%Y")
        if date in chats[chats_id]['massages']:
            pass
        else:
            chats[chats_id]['massages'].append(f"               {date}")
        user_file: dict = self.read_to_file(self._user_file)
        massage = input("Massage: ")
        name = f"{user_file[username]["full_name"]}:{chass_and_minute}"
        sms = f"{massage} -> {name}"
        chats[chats_id]["massages"].append(sms)
        self.write_to_file(self._chats, chats)
        self.show_menu_chats(chats_id, username)

    def show_all_massages(self, chat_id, username):
        chats: dict = self.read_to_file(self._chats)
        try:
            print(json.dumps(chats[chat_id]['massages'], indent=4))
        except KeyError:
            print("no choice chats history")
            return self.show_menu_chats(chat_id, username)
        except ValueError:
            print('no choice chats history')
            return self.show_menu_chats(chat_id, username)
