import json
import os


def int_input(prompt=""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error.")


class JsonManager:
    def __init__(self):
        self._student_file = "files/Student.json"
        self._admin_file = "files/Admin.json"
        self._teacher_file = "files/Teacher.json"
        self._super_admin = "files/Super.json"

    def __str__(self):
        pass

    def add_to_file(self, json_file, data):
        files = self.read_to_file(json_file)
        files.update(data)
        self.write_to_file(json_file, files)

    def read_to_file(self, json_file):
        try:
            if os.path.exists(json_file):
                with open(file=json_file, mode="r", encoding="UTF-8") as file:
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

    def write_to_file(self, json_file, user):
        with open(file=json_file, mode="w", encoding="UTF-8") as file:
            json.dump(user, file, indent=4)
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

    def phone_input(self, txt: str):
        self.__str__()
        while True:
            phone: int = int_input(txt)
            if 900000000 <= phone <= 999999999:
                return phone
            else:
                print("exp:918743565...")

    def grade_input(self, txt: str):
        self.__str__()
        while True:
            grade: int = int_input(txt)
            if 0 <= grade <= 5:
                return grade
            else:
                print("0 <= grade <= 5")
