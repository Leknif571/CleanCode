from Controller.game_controller import GameController

def main():
    controller = GameController()  # Crée une instance de GameController
    controller.play_games()  # Lancer la logique du jeu

if __name__ == "__main__":
    main()