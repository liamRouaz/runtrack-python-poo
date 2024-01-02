class Operation:
    #init = constructeur
    def __init__(self, nombre1 = 12, nombre2 = 3):
    #self = parametre a place en premier pour chaque methode y faire reference a l'instance de classe (ex:self)
        self.nombre1 = nombre1
        self.nombre2 = nombre2

#instance est l'obj creé a partire de la classe operation
#instantation de la classe
operation_instance = Operation()

#resulta de la classe
print ("le nombre1 est " + str (operation_instance.nombre1))
print ("le nombre2 est " + str (operation_instance.nombre2))




        
    
