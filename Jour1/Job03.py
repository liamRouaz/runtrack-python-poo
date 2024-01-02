class MonObjet:
    def __init__(self, value, value2):
        self.nombre_value = value
        self.nombre_value2 = value2

 
    def add(self):
        print(self.nombre_value + self.nombre_value2)

#valeur de la classe 

addition = MonObjet(10, 3) 
addition.add()