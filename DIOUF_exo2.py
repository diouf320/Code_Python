from robot import Robot

class Human():
    def __init__(self, sexe):
        self.sexe = sexe
        self.aliments_manges = []

    def manger(self, *aliments):
        self.aliments_manges.extend(aliments)
        print(f"Il a mangé : {aliments}")

    def digerer(self):
        if not self.aliments_manges:
            print("l'estomac est vide")
        else:
            aliments_digeres = self.aliments_manges
            self.aliments_manges.clear()
            print("Les aliments ont été digérés")

       
class Cyborg(Robot, Human):   
    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        print(f"le cyborg est : {sexe}\n")

cyborg = Cyborg("Cyborg","Homme")
cyborg.digerer()
cyborg.manger("orange","pomme")
cyborg.digerer()

cyborg.charger()
cyborg.allumer()
cyborg.set_current_speed(10)
print(cyborg.get_etat())
