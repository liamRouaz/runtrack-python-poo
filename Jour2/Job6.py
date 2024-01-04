class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}  # Utilisation d'un dictionnaire pour représenter les plats
        self._statut_commande = "En cours"

    # Méthode privée pour calculer le total de la commande
    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
        print(f"Plat {nom_plat} ajouté à la commande.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self._statut_commande = "Annulée"
        print("La commande a été annulée.")

    # Méthode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        print(f"Commande {self._numero_commande}:")
        for nom_plat, details_plat in self._plats_commandes.items():
            print(f"{nom_plat} - {details_plat['prix']} € - Statut: {details_plat['statut']}")
        total = self._calculer_total()
        print(f"Total à payer: {total} €")

    # Méthode pour calculer la TVA
    def calculer_tva(self):
        total = self._calculer_total()
        tva = total * 0.20  # Supposons une TVA de 20%
        return tva


# Utilisation de la classe Commande
commande1 = Commande(numero_commande=1)

# Ajouter des plats à la commande
commande1.ajouter_plat("Pizza", 10.99)
commande1.ajouter_plat("Salade", 5.99)

# Afficher la commande
commande1.afficher_commande()

# Calculer et afficher la TVA
tva = commande1.calculer_tva()
print(f"TVA à payer: {tva} €")

# Annuler la commande
commande1.annuler_commande()
