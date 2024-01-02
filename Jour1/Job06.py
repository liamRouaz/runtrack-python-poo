class Animal:
    def __init__(self, age):
        self.age = age
 
    def __add__(self, other):
        return Animal(self.age + other)

    def nommer(self, nomdlabete):
        self.nomdlabete = nomdlabete
        
 
age_animal = Animal(0)
 
age_animal_2 = age_animal
 
age_animal += 1

age_animal.nommer("lola")

print("l'age de l'animal" , age_animal.age)   
print("l'age de l'animal" , age_animal_2.age)  
print("l'animal se nomme ", age_animal.nomdlabete)