class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = 50

    # Assesseurs
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    def get_reservoir(self):
        return self._reservoir

    # Mutateurs
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self._en_marche = en_marche

    # Méthodes
    def demarrer(self):
        if self.verifier_plein():
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est trop bas. La voiture ne peut pas démarrer.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    # Méthode privée
    def verifier_plein(self):
        return self._reservoir > 5


# Utilisation de la classe Voiture
ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2020, kilometrage=30000)

# Accéder à des attributs
print("Marque de la voiture:", ma_voiture.get_marque())
print("En marche:", ma_voiture.get_en_marche())
print("Niveau du réservoir:", ma_voiture.get_reservoir())

# Démarrer la voiture
ma_voiture.demarrer()

# Arrêter la voiture
ma_voiture.arreter()
