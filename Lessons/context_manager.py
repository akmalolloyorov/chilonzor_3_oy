import json


class CustomOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.file.close()


def add_to_file(file_name,):
    with CustomOpen(filename="c.json", mode="w") as file:
        print("hello world")
        u = {"hello": "world"}
        json.dump(u, file, indent=4)
