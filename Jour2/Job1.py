class Rectangle:
    def __init__(self, longueur=10, largeur=5):
        #self = variable servent a faire reference a linstance de classe
        #valeur ajouter au parametre "longeur"
        self.longueur = longueur
        self.largeur = largeur

    # getters pour récupérer les valeurs
    def get_longueur(self):
        return self.longueur

    def get_largeur(self):
        return self.largeur

    # setters pour modifier les valeurs
    def set_longueur(self, nouvelle_longueur):
        self.longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur

# appel du constructeur
rectangle_instance = Rectangle()

# affichage des valeurs initiales
print("Longueur : ", rectangle_instance.get_longueur())
print("Largeur : ", rectangle_instance.get_largeur())

# modification des valeurs à l'aide des setters
rectangle_instance.set_longueur(15)
rectangle_instance.set_largeur(7)

# affichage des nouvelles valeurs
print("Nouvelle longueur : ", rectangle_instance.get_longueur())
print("Nouvelle largeur : ", rectangle_instance.get_largeur())
