import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.total_attempts = 0
        self.current_attempts = 0

    def get_secret_number(self):
        """Retourne le nombre secret."""
        return self.secret_number

    def increment_total_attempts(self):
        """Incrémente le nombre total d'essais."""
        self.total_attempts += 1

    def increment_current_attempts(self):
        """Incrémente le nombre d'essais en cours."""
        self.current_attempts += 1

    def reset_current_attempts(self):
        """Réinitialise le nombre d'essais en cours."""
        self.current_attempts = 0
