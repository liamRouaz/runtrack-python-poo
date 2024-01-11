import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.subir_degats(degats)

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0
        print(f"{self.nom} a subi {degats} points de dégâts. Points de vie restants : {self.vie}")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        print("Choisissez le niveau de difficulté :")
        print("1. Facile")
        print("2. Normal")
        print("3. Difficile")
        choix = input("Entrez le numéro du niveau : ")
        if choix == "1":
            self.niveau = 1
        elif choix == "2":
            self.niveau = 2
        elif choix == "3":
            self.niveau = 3
        else:
            print("Niveau non valide. Niveau par défaut : Normal (2)")

    def lancerJeu(self):
        self.choisirNiveau()

        joueur = Personnage("Joueur", self.niveau * 20)
        ennemi = Personnage("Ennemi", self.niveau * 15)

        print(f"Un ennemi redoutable apparaît ! Niveau de difficulté : {self.niveau}")
        print(f"{joueur.nom} - Points de vie : {joueur.vie}")
        print(f"{ennemi.nom} - Points de vie : {ennemi.vie}\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie > 0:
                ennemi.attaquer(joueur)

        self.afficherResultat(joueur, ennemi)

    def afficherResultat(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("Vous avez perdu. Le héros est vaincu.")
        elif ennemi.vie <= 0:
            print("Félicitations ! Vous avez vaincu l'ennemi. Victoire !")
        print(f"{joueur.nom} - Points de vie restants : {joueur.vie}")
        print(f"{ennemi.nom} - Points de vie restants : {ennemi.vie}")

# Création de l'instance du jeu
jeu = Jeu()

# Lancer le jeu
jeu.lancerJeu()
