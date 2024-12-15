class Player:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0

    def get_name(self):
        """Retourne le nom du joueur."""
        return self.name

    def get_games_played(self):
        """Retourne le nombre de parties jouées."""
        return self.games_played

    def get_games_won(self):
        """Retourne le nombre de parties gagnées."""
        return self.games_won

    def set_name(self, name):
        """Modifie le nom du joueur."""
        self.name = name

    def increment_games_played(self):
        """Incrémente le nombre de parties jouées."""
        self.games_played += 1

    def increment_games_won(self):
        """Incrémente le nombre de parties gagnées."""
        self.games_won += 1
