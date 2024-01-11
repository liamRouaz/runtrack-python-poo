class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte {self.__numero_compte} - {self.__nom} {self.__prenom}")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué.")
            self.afficherSolde()
        else:
            print("Solde insuffisant. Opération annulée.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Des agios de {agios} € ont été appliqués.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
        else:
            print("Solde insuffisant. Virement annulé.")


# Création d'une première instance de la classe CompteBancaire
compte1 = CompteBancaire("123456", "Doe", "John", 1000)

# Affichage du détail du compte
compte1.afficher()

# Versement sur le compte
compte1.versement(500)

# Retrait du compte
compte1.retrait(300)

# Création d'une deuxième instance de la classe CompteBancaire à découvert
compte2 = CompteBancaire("654321", "Smith", "Alice", -200, decouvert=True)

# Virement du compte1 vers le compte2 pour remettre à zéro le solde du compte2
compte1.virement(compte2, 800)

# Application d'agios sur le compte2
compte2.agios(0.05)
