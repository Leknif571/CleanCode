class Player:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0

    def get_name(self):
        return self.name

    def get_games_played(self):
        return self.games_played

    def get_games_won(self):
        return self.games_won

    def set_name(self, name):
        self.name = name

    def increment_games_played(self):
        self.games_played += 1

    def increment_games_won(self):
        self.games_won += 1
