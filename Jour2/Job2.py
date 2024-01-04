class Livre:
    def __init__(self,titre,auteur,page):
        #attribut privés
        self.titre = titre
        self.auteur = auteur
        self.page = page
        

    #getter pour recuperer les valeur des attribut
    def get_ile(self):
        return self.titre
    def get_Aldous_huxley(self):
        return self.auteur
    def get_page(self):
        return self.page
    
    #setter pour modifier les valeur privés
    def set_page(self, page_livre_de_poche):
        self.page = page_livre_de_poche

Livre_instance = Livre(titre = "Retour au meilleur des mondes", auteur ="d'Aldous Huxley", page = 155)

print("Titre : ", Livre_instance.get_ile())
print("Auteur : ", Livre_instance.get_Aldous_huxley())
print("Nombre de page : ", Livre_instance.get_page())

Livre_instance.set_page(400)

print("Titre : ", Livre_instance.get_ile())
print("Auteur : ", Livre_instance.get_Aldous_huxley())
print("Nombre de page : ", Livre_instance.get_page())




        
