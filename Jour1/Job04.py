class Personne:
    def __init__(self, nom = "Dupond", prenom = "jean", nom2="Doe", prenom2="John"):
        self.nom = nom
        self.prenom = prenom
        self.nom2 = nom2
        self.prenom2 = prenom2

    def Presentation(self):
        print("Je suis", self.nom, self.prenom)
        print("Je suis", self.nom2, self.prenom2)

# Instanciation de la classe avec deux arguments
John = Personne("Doe", "John")
Jean = Personne("Dupond", "Jean")
# Appel de la méthode Presentation
John.Presentation()
Jean.Presentation()
