import hashlib,time

users = {
    "akmal2004": {
        "full_name": "Akmal Olloyorov",
        "password": "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d",
        "my_joined": []
    },
    "tima": {
        "full_name": "Temur",
        "password": "4e07408562bedb8b60ce05c1decfe3ad16b7223096 7de01f640b7e4729b49fce",
        "my_joined": []
    }
}


class Main:
    @staticmethod
    def my_decorator(func):
        def wrapper():
            name = input('Enter your name: ').title()
            username = input("username: ")
            parol = input('password')
            p = hashlib.sha256(parol.encode()).hexdigest()
            if name in users.keys():
                print("bu odam oldindan bor.")
                return
            else:
                func(name, username, p)

        return wrapper()

    @my_decorator
    def register(self, name, username, parol):
        user = {
            username: {
                "full_name": name,
                "password": parol,
                "my_joined": []
            }
        }
        users.update(user)


m = Main()
m.register()
