	
from abc import ABCMeta, abstractmethod

class Vehicule(metaclass=ABCMeta):
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def get_vehicule(self):
        print(f"Véhicule : {self.name}, Type : {self.type}")

class UnmannedVehicule(Vehicule):
    def __init__(self,name):
        super().__init__(name,type="Autonomous")

    @abstractmethod
    def mission(self):
        pass

class AerialVehicule(Vehicule):
    def __init__(self,name):
        super().__init__(name,type="Aérien")

    def fly(self):
        print(f"{self.name} vole dans le ciel")

class GroundVehicule(Vehicule):
    def __init__(self,name):
        super().__init__(name,type="terrestre")

    def drive(self):
        print(f"{self.name} roule sur le terrain")

class UnderseaVehicule(Vehicule):
    def __init__(self,name):
        super().__init__(name,type="Sous_marin")

    def swim(self):
        print(f"{self.name} plonge sous l'eau")

class UAV(UnmannedVehicule,AerialVehicule):
    def __init__(self,name):
        UnmannedVehicule.__init__(self,name)
        AerialVehicule.__init__(self,name)

    def mission(self):
        print(f"{self.name} est en mission aérienne")
        self.fly()

class UUV(UnmannedVehicule,UnderseaVehicule):
    def __init__(self,name):
        UnmannedVehicule.__init__(self,name)
        UnderseaVehicule.__init__(self,name)
        

    def mission(self):
        print(f"{self.name} est en mission sous-marine")
        self.swim()

class UGV(UnmannedVehicule,GroundVehicule):
    def __init__(self,name):
        UnmannedVehicule.__init__(self,name)
        GroundVehicule.__init__(self,name)
        
    def mission(self):
        print(f"{self.name} est en mission terrestre")
        self.drive()

def mission_vehicule(vehicule):
    vehicule.mission()

uav = UAV()
ugv = UGV()
uuv = UUV()

mission_vehicule(uav)
mission_vehicule(ugv)
mission_vehicule(uuv)
