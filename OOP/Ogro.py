from Enemigo import *

class Ogro(Enemigo):

    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("¡Ogro aplastar todo!!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
    funciona_ataque_especial = random.random() < 0.50
    if funciona_ataque_especial:
        self.puntos_energia += 2
        print("Zombie ha regenardo su energia con 2HP!")