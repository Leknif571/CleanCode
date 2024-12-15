from Model.game import Game
from Model.player import Player
from View.game_view import GameView

class GameController:
    def __init__(self):
        self.view = GameView()
        self.game = Game()
        self.player = Player(self.view.prompt_player_name())

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
        """Joue au jeu de devinettes."""
        self.game.reset_current_attempts()  # Réinitialise les tentatives en cours
        self.game.increment_total_attempts()  # Incrémente les tentatives totales
        self.player.increment_games_played()  # Incrémente le nombre de parties jouées
        print(f"L'ordinateur a choisi un nombre entre 1 et 100.")
        
        while True:
            guess = self.view.prompt_guess()  # Demande au joueur de deviner
            self.game.increment_current_attempts()  # Incrémente les tentatives en cours
            feedback = self.get_feedback(guess)
            self.view.display_feedback(feedback)
            
            if feedback == "Correct":
                self.view.display_congratulations(self.player.get_name(), self.game.current_attempts)
                self.player.increment_games_won()  # Si le joueur gagne, on incrémente le nombre de parties gagnées
                break

    def get_feedback(self, guess):
        """Retourne le feedback par rapport au nombre proposé."""
        secret_number = self.game.get_secret_number()
        
        if guess < secret_number:
            return "Plus grand"
        elif guess > secret_number:
            return "Plus petit"
        else:
            return "Correct"
