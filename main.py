class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print("Qo'ng'iroq qilinmoqda...")

class Smartphone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def call(self):
        super().call()
        print(f"{self.os} orqali internet qo'ng'irog'i amalga oshirildi")
