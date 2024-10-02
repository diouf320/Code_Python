import time
print(time.time())

class Robot():
    def __init__(self, name = "unnamed"):
        self.__name = name
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0
        self.__states = ['shutown', 'running']

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def allumer(self):
        if self.__battery_level > 0:
            self.__power = True
            print(f"{self.__name} est allumé")
        else:
            print("La batterie est vide")

    def eteindre(self):
        self.__power = False
        self.__current_speed = 0
        print(f"{self.__name} est éteint")

    def charger(self):
        while self.__battery_level < 100:
            self.__battery_level += 10
            if self.__battery_level > 100:
                self.__battery_level = 100
            print(f"La batterie est à : {self.__battery_level}%")
            time.sleep(1)
        print("Chargement complet")

    def get_battery(self):
        return self.__battery_level

    def set_current_speed(self, current_speed):
        if self.__power:
            self.__current_speed = current_speed
            print(f"Vitesse : {current_speed}")
        else:
            print(f"{self.__name} est éteint")

    def get_current_speed(self):
        return self.__current_speed

    def stop(self):
        self.__current_speed = 0
        print(f"{self.__name} est arrêté")

    def get_state(self):
        if self.__power:
            return self.__states[1]
        else:
            return self.__states[0]
        
    def get_etat(self):
        state = self.get_state()
        return print(f"{self.__name}:\n Etat: {state}\n Batterie: {self.__battery_level}\n Vitesse: {self.__current_speed}\n")
    

robot = Robot()
robot.set_name("NOVA")
robot.charger()
robot.allumer()
robot.set_current_speed(10)
print(robot.get_name())
print(robot.get_battery())
print(robot.get_current_speed())
print(robot.get_state())
print(robot.get_etat())
robot.stop()
robot.eteindre()
print(robot.get_name())
print(robot.get_battery())
print(robot.get_current_speed())
print(robot.get_state())
print(robot.get_etat())
