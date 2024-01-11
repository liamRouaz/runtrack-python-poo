class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée : {tache}")

    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche supprimée : {tache}")
        else:
            print("La tâche n'existe pas dans la liste.")

    def marquerCommeFinie(self, tache):
        for t in self.taches:
            if t.titre == tache.titre and t.description == tache.description:
                t.statut = "Terminée"
                print(f"Tâche marquée comme terminée : {t}")
                return
        print("La tâche n'existe pas dans la liste.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list


# Test du code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Chapitres 1 à 3")
tache3 = Tache("Nettoyer la maison", "Aspirer et passer la serpillère")

liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste des tâches
liste_taches.afficherListe()

# Marquer une tâche comme terminée
liste_taches.marquerCommeFinie(tache2)

# Supprimer une tâche
liste_taches.supprimerTache(tache3)

# Affichage de la liste des tâches à faire
taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)
