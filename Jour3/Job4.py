class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but!")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a réalisé une passe décisive!")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge et est exclu du match.")

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (Numéro {self.numero}, Position : {self.position}):")
        print(f"Buts marqués : {self.buts_marques}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}")
        print("\n")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Modric", 8, "Milieu")
joueur4 = Joueur("Van Dijk", 4, "Défenseur")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques avant le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()
joueur4.recevoirUnCartonRouge()

# Mise à jour des statistiques après le match
equipe1.mettreAJourStatistiquesJoueur("Messi", "but")
equipe2.mettreAJourStatistiquesJoueur("Ronaldo", "passe")
equipe1.mettreAJourStatistiquesJoueur("Modric", "carton_jaune")
equipe2.mettreAJourStatistiquesJoueur("Van Dijk", "carton_rouge")

# Affichage des statistiques après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
