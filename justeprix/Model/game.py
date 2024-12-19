import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.total_attempts = 0
        self.current_attempts = 0

    def get_secret_number(self):
        return self.secret_number

    def increment_total_attempts(self):
        self.total_attempts += 1

    def increment_current_attempts(self):
        self.current_attempts += 1

    def reset_current_attempts(self):
        self.current_attempts = 0
    
    def set_secret_number(self):
        self.secret_number = random.randint(1,100)
