class GameView:
    def __init__(self):
        pass

    def prompt_player_name(self):
        """Demande au joueur son nom."""
        return input("Entrez votre nom : ")

    def prompt_guess(self):
        """Demande au joueur de proposer un nombre."""
        try:
            return int(input("Proposez un nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return self.prompt_guess()

    def display_feedback(self, feedback):
        """Affiche les indices pour le joueur."""
        print(feedback)

    def display_congratulations(self, player_name, attempts):
        """Affiche la victoire du joueur."""
        print(f"Bravo {player_name} ! Vous avez trouvé le nombre en {attempts} essais.")
