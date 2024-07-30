import random
import json

from chats import Chats, int_input


class User(Chats):
    def show_menu_user(self, username):
        text = """
        1. Create chat | chat_code -> chat random id
        2. Join chat | -> chat_id, chat_name
        3. Delete chat | username
        4. Show my created chats
        5. Show my joined chats
        6. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.create_chat(username)
        elif num == 2:
            self.join_chat(username)
        elif num == 3:
            self.delete_chat(username)
        elif num == 4:
            self.show_my_created_chat(username)
        elif num == 5:
            self.show_my_joined_chat(username)
        else:
            return 6

    def create_chat(self, username):
        chat_name = input("Chat name: ")
        chat_file: dict = self.read_to_file(self._chats)
        try:
            chat_id = random.randint(100000, 999999)
            while chat_file[username]["chat_id"] == chat_id:
                chat_id = random.randint(100000, 999999)
        except KeyError:
            chat_id = random.randint(100000, 999999)
        chat = {
            chat_id: {
                "username": username,
                "chat_name": chat_name,
                "massages": [f"             {chat_name}"]
            }
        }
        self.write_to_file(self._chats, chat)
        print(f'you {chat_name}-group id-{chat_id} ')
        if self.show_menu_chats(chat_id, username) == 3:
            return self.show_menu_user(username)
        self.add_to_file(self._chats, chat)

    def join_chat(self, username):
        user_file = self.read_to_file(self._user_file)
        chat_name = input("Chat name: ")
        chat_id = input("Chat id: ")
        chats: dict = self.read_to_file(self._chats)
        try:
            if chats[chat_id]['chat_name'] == chat_name:
                if f"chat name-{chat_name}" in user_file[username]["my_joined"]:
                    pass
                else:
                    user_file[username]["my_joined"].append(f"chat name-{chat_name}")
                self.write_to_file(self._user_file, user_file)
                if self.show_menu_chats(chat_id, username) == 3:
                    return self.show_menu_user(username)
            else:
                print("Wrong input. chat name or chat id error..")
                return self.show_menu_user(username)
        except KeyError:
            self.show_menu_user(username)

        except ValueError:
            self.show_menu_user(username)

    def delete_chat(self, username):
        chat_list = []
        chat_id = 0
        chats: dict = self.read_to_file(self._chats)
        try:
            for i, j in chats.items():
                if j['username'] == username:
                    chat_list.append(f"{j['chat_name']}, chat id-{i}")
            chat = self.list_choice(chat_list)
            for i in chats.keys():
                if i in chat:
                    chat_id = i
            del chats[chat_id]
            self.write_to_file(self._chats, chats)
        except KeyError:
            print("no choice chat...")
        except ValueError:
            print('no choice chat...')

    def show_my_created_chat(self, username):
        chat_list = []
        chats: dict = self.read_to_file(self._chats)
        try:
            for i, j in chats.items():
                if j['username'] == username:
                    chat_list.append(f"{j['chat_name']}, chat id-{i}")
            print(json.dumps(chat_list, indent=4))
        except KeyError:
            print("no choice chat...")
        except ValueError:
            print('no choice chat...')

    def show_my_joined_chat(self, username):
        users: dict = self.read_to_file(self._user_file)
        try:
            print(json.dumps(users[username]['my_joined'], indent=4))
        except KeyError:
            print("No choice joined chat")
        except ValueError:
            print('No choice joined chat')
