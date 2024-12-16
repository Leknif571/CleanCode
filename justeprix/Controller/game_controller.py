from Model.game import Game
from Model.player import Player
from View.game_view import GameView

class GameController:
    def __init__(self):
        self.view = GameView()
        self.game = Game()
        self.player = Player(self.view.enter_player_name())

    def play_games(self):
        retry = True
        while retry :
            self.play_game()
            replay = input("Veux-tu jouer à nouveau ? (O/N) : ").strip().lower()
            if replay == 'o':
                retry = True
            elif replay == 'n':
                retry = False
            else:
                print("Réponse invalide, tape 'o' ou 'n'.")
            

    def play_game(self):
        self.game.reset_current_attempts()
        self.game.increment_total_attempts()
        self.player.increment_games_played()
        print(f"L'ordinateur a choisi un nombre entre 1 et 100.")
        
        while True:
            guess = self.view.enter_guess() 
            self.game.increment_current_attempts() 
            response = self.return_response(guess)
            self.view.display_return_response(response)
            
            if response == "Correct":
                self.view.display_congratulations(self.player.get_name(), self.game.current_attempts)
                self.player.increment_games_won() 
                break

    def return_response(self, guess):
        secret_number = self.game.get_secret_number()
        
        if guess < secret_number:
            return "Plus grand"
        elif guess > secret_number:
            return "Plus petit"
        else:
            return "Correct"
