import random


class RandomMail:
    @staticmethod
    def generate_mail():
        symbols = random.randint(1, 9999)
        email = f'name{symbols}@mail.ru'
        return email
