class Student:
    def __init__(self, nom, prenom, numero_etudiant,credit,add_credit):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiant = numero_etudiant
        self.credit = credit
        self.add_credit =add_credit
        
        #get pour enregistre les valeur des paramettre
    def get_nom(self):
        return self.nom 
    def get_prenom(self):
        return self.prenom
    def get_numero_etudiant(self):
        return self.numero_etudiant
    def get_credit(self):
        return self.credit
    def get_add_credit(self):
        return self.add_credit
    
    #set pour rajouter des valeur (dans cette ligne ci dessou ont cret une variable set credit pour attribuer une valeur au credit)
    #toujours mettre le paramettre priver dans les parantese
    def set_add_credit(self, add_credit):
        self.add_credit = add_credit


Student_instance= Student(nom="rouaz", prenom="", numero_etudiant="",credit=0,add_credit=0)
print ("nom = ",Student_instance.get_nom())
print ("credits",Student_instance.get_credit())
Student_instance.set_add_credit(0)
print ("credits",Student_instance.get_add_credit())

# Instancier un objet représentant l’étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student(nom="Doe", prenom="John", numero_etudiant="145", credit=0, add_credit=0)

# Ajoutez-lui des crédits à trois reprises
john_doe.set_add_credit(30)
john_doe.set_add_credit(20)
john_doe.set_add_credit(25)

# Imprimez son total de crédits en console
print("Total des crédits de John Doe:", john_doe.get_credit() + john_doe.get_add_credit())
