import json
import os
from datetime import datetime
from contextlib import contextmanager

"""
1. O'zingiz customning conetxt manager yarating va u orqali orders.json fayni oching.
Foydalanuvchidan ism, yosh, tug'ilgan kun malumotlarini so'rang va ularni faylga yozing.
(Context managerni ham funksiya orqali ham class orqali yasab yeching)

"""


@contextmanager
def custom_open(filename, mode):
    file = open(filename, mode, encoding="UTF-8")
    yield file
    file.close()


# This is the CustomOpen
class CustomOpen:
    def __init__(self, filename, mode, encoding="UTF-8"):
        self.filename = filename
        self.encoding = encoding
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(file=self.filename, mode=self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# This is function custom_open


def int_input(prompt=""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error.")


class JsonManager:
    def __init__(self):
        self.users_file = "orders.json"

    def __str__(self):
        pass

    def add_to_file(self, json_file: str, data: dict) -> None:
        files: dict = self.read_to_file(json_file)
        files.update(data)
        self.write_to_file(json_file, files)

    def read_to_file(self, json_file: str) -> dict:
        try:
            if os.path.exists(json_file):
                """with custom_open(filename="test", mode="r") as read_for:
                    files = json.load(json_file)"""
                with CustomOpen(filename=json_file, mode="r") as file:
                    files: dict = json.load(file)
                    self.__str__()
                    return files
            else:
                self.__str__()
                files = {}
                return files
        except json.decoder.JSONDecodeError:
            files = {}
            return files

    def write_to_file(self, json_file: str, data: dict) -> None:
        """with custom_open(filename="test", mode="w") as write_for:
            json.dump(data, write_for, indent=4)"""
        with CustomOpen(filename=json_file, mode="w") as file:
            json.dump(data, file, indent=4)
        return self.__str__()

    def list_choice(self, user_list: list) -> str or int:
        x_list = ["choice number"]
        y_list = []
        count = 0
        count_list = []
        for key, value in enumerate(user_list, 1):
            x_list.append(f"{key}. {value}")
            y_list.append(value)
            count += 1
            count_list.append(count)
        print(json.dumps(x_list, indent=4))
        while True:
            try:
                num: int = int(input("number="))
                if num in count_list:
                    self.__str__()
                    return y_list[num - 1]
                else:
                    print('wrong input')
            except ValueError:
                print("incorrect , only number.")

    def current_time(self):
        self.__str__()
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
