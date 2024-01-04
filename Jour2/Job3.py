class Livre:
    def __init__(self,titre,auteur,page,disponible,emprunter,rendre):
        #attribut privés
        self.titre = titre
        self.auteur = auteur
        self.page = page
        self.disponible = disponible
        disponible = True
        self.emprunter = emprunter
        if emprunter == True:
            disponible == False
        self.rendre = rendre

        

    #getter pour recuperer les valeur des attribut
    def get_ile(self):
        return self.titre
    def get_Aldous_huxley(self):
        return self.auteur
    def get_page(self):
        return self.page
    def get_disponible(self):
        return self.disponible
    def get_emprunter(self):
        return self.emprunter
    def get_rendre(self):
        return self.rendre
    
    #setter pour modifier les valeur privés
    def set_page(self, page_livre_de_poche):
        self.page = page_livre_de_poche
    def set_disponible(self, disponible):
        self.disponible = disponible

Livre_instance = Livre(titre = "Retour au meilleur des mondes", auteur ="d'Aldous Huxley", page = 155,disponible ="oui", emprunter ="oui", rendre="non rendu")

print("Titre : ", Livre_instance.get_ile())
print("Auteur : ", Livre_instance.get_Aldous_huxley())
print("Nombre de page : ", Livre_instance.get_page())
Livre_instance.set_page(400)

print("Titre : ", Livre_instance.get_ile())
print("Auteur : ", Livre_instance.get_Aldous_huxley())
print("Nombre de page : ", Livre_instance.get_page())

print("emprunter : ",Livre_instance.get_emprunter())
Livre_instance.set_disponible("non")
print("disponibiliter : ",Livre_instance.get_disponible ())
print("rendu ? :",Livre_instance.get_rendre())


        
