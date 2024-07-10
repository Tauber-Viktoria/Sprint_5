import random


class RandomMail:
    @staticmethod
    def generate_mail():
        symbols = random.randint(1, 9999)
        mail = f'name{symbols}@mail.ru'
        return mail


