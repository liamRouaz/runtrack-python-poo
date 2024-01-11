class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nouveau_nombre):
        self.__nombre_habitants = nouveau_nombre


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        nombre_habitants_actuel = self.__ville.get_nombre_habitants()
        self.__ville.set_nombre_habitants(nombre_habitants_actuel + 1)


# Création d'objets Ville
ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants de chaque ville
print(f"Nombre d'habitants à {ville_paris.get_nom()}: {ville_paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {ville_marseille.get_nom()}: {ville_marseille.get_nombre_habitants()}")

# Création d'objets Personne
john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

# Ajout d'une personne à la population de sa ville
john.ajouter_population()

# Affichage du nombre d'habitants de chaque ville après l'ajout de John
print(f"mise à jours de la population {ville_paris.get_nom()}: {ville_paris.get_nombre_habitants()}")
print(f"mise à jours de la population {ville_marseille.get_nom()}: {ville_marseille.get_nombre_habitants()}")
