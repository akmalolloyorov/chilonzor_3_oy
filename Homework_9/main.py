"""
2. Tasavvuring qiling sizda buyurtmalar saqlangan fayl bor orders.json, va uni ichida bazi
   bir buyurtmalar ikki marttadan takrorlanib ketgan sizni vazifangiz takrorlanib ketgan
   buyurtmalarni faqat bittasini olib qolish,
   agar zakazni user, total_price, products qismlari teng bo'lsa demak bular bir xil
   ulardan istalgan birini olib qolishingiz mumkin
   (o'zingiz yozgan cntext managerdan foydalaning)
   orders.json

"""
from context_manager import JsonManager


class Checkout(JsonManager):
    def __init__(self):
        super().__init__()
        self.user = None
        self.total_price = None
        self.products = None
        self.user_id = {}

    # generator function ⬇️
    def check(self):
        files: dict = self.read_to_file(self.users_file)
        for i in files.keys():
            self.user_id = {i: files[i]}
            self.user = files[i]['user']
            self.total_price = files[i]["total_price"]
            self.products = files[i]["products"]
            for j in files.keys():
                if i == j:
                    pass
                else:
                    if files[j]["user"] == self.user and files[j]['total_price'] == self.total_price:
                        if files[j]["products"] == self.products:
                            yield j, self.user_id

    def clean_up(self):
        files: dict = self.read_to_file(self.users_file)
        for i, j in self.check():
            del files[i]
            files.update(j)
        self.write_to_file(self.users_file, files)


d = Checkout()
d.clean_up()
