class GameView:
    def __init__(self):
        pass

    def enter_player_name(self):
        return input("Entrez votre nom : ")

    def enter_guess(self):
        try:
            return int(input("Proposez un nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return self.enter_guess()

    def display_return_response(self, feedback):
        print(feedback)

    def display_congratulations(self, player_name, attempts):
        print(f"Bravo {player_name} ! Vous avez trouvé le nombre en {attempts} essais.")
    
