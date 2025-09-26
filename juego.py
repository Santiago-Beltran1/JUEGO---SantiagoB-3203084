class Jugadores:
    def __init__(self, nombre, categoria, arma, daño, item, vida):
        self.nombre = nombre
        self.categoria = categoria
        self.arma = arma
        self.daño = daño
        self.item = item
        self.vida = vida
    def saludar (self):
        print(f"Hola {self.nombre} bienvenido al juego")


personaje1 = Jugadores("J1", "killer", "Shurikens", 9.5, "Frasco de furia", 30)
personaje2 = Jugadores("J2", "support", "Bate", 2.5, "Frasco de estamina", 80)
personaje3 = Jugadores("J3", "piromante", "Magia Oscura", 6.5, "Frasco aumentador de piromancia", 60)
personaje4 = Jugadores("J4", "selva", "Dagas", 4.0, "Energizante", 70)
personaje5 = Jugadores("J5", "bandido", "cuchilla normal", 7.5, "Capa de Invisibilidad", 50)
personaje6 = Jugadores("J6", "tanque", "Hacha Gigante", 5.0, "Dureza Extrema", 100)


print(personaje1.nombre, personaje1.categoria, personaje1.arma, personaje1.daño, personaje1.item, personaje1.vida)
print(personaje2.nombre, personaje2.categoria, personaje2.arma, personaje2.daño, personaje2.item, personaje2.vida)
print(personaje3.nombre, personaje3.categoria, personaje3.arma, personaje3.daño, personaje3.item, personaje3.vida)
print(personaje4.nombre, personaje4.categoria, personaje4.arma, personaje4.daño, personaje4.item, personaje4.vida)
print(personaje5.nombre, personaje5.categoria, personaje5.arma, personaje5.daño, personaje5.item, personaje5.vida)
print(personaje6.nombre, personaje6.categoria, personaje6.arma, personaje6.daño, personaje6.item, personaje6.vida)

personaje1.saludar()
personaje2.saludar()
personaje3.saludar()
personaje4.saludar()
personaje5.saludar()
personaje6.saludar()

class juego:
    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
    def p1(self):
        

print("---!BIENVENIDO AL JUEGO: ELIJA 3 TIPOS DE PERSONAJE (Puede repetir) PARA LUCHAR CONTRA LA CPU!---")
        

        