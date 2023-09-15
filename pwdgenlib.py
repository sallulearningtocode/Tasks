import random
import string

class PasswordGenerator:
    def __init__(self):
        self.password = ''

    def generate_password(self, length=8, include_symbols=False):
        characters = string.ascii_letters + string.digits
        if include_symbols:
            characters += string.punctuation
        self.password = ''.join(random.choice(characters) for _ in range(length))
        return self.password

    def get_password(self):
        return self.password
