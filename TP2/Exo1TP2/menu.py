from notebook import Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        
        self.choix = {
            "1": self.ajouter_note,
            # "2": self.afficher_notes,
            # "3": self.rechercher_note,
            # "4": self.consulter_note,
            "5": self.quitter
        }

    def afficher_menu(self):
        print("""
        1. Ajouter une note
        2. Afficher les notes
        3. Rechercher une note
        4. Consulter une note
        5. Quitter le programme
        """)
    
    def ajouter_note(self):
        '''
        Cette methode permet d'ajouter une note
        '''
        memo = input("Entrez le contenur de la note:")
        balises = input("Entrez les balises (séparées par des virgules): ")
        self.notebook.ajouter_note(memo, balises)
        print("La note a été ajoutée avec succès!")

    def quitter(self):
        print("Merci d'avoir utilisé le programme")
        exit(0);

    def run(self):
        while True:
            self.afficher_menu()
            choix_option = input("Entre un choix:")
            action = self.choix.get(choix_option)
            if action:
                action()
            else:
                print("Choix invalide!")