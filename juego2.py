import random

class Jugador:
    def __init__(self, nombre, categoria, arma, daño, item, vida):
        self.nombre = nombre
        self.categoria = categoria
        self.arma = arma
        self.daño = daño
        self.item = item
        self.vida = vida
        self.item_usado = False
        self.quemado = 0
        self.invulnerable = False
        self.defensa = False
        self.furia_activa = False
        self.extra_turno = False

    def mostrar_stats(self):
        estado = f"{self.nombre} | Vida: {self.vida:.1f} | Arma: {self.arma} | Daño: {self.daño}"
        if self.item_usado:
            estado += " | Item usado"
        else:
            estado += f" | Item: {self.item}"
        print(estado)

    def usar_item(self):
        if self.item_usado:
            print(f"{self.nombre} ya usó su item.")
            return

        print(f"🛠️ {self.nombre} usa {self.item}!")
        self.item_usado = True

        if self.item == "Frasco de furia":
            self.furia_activa = True
        elif self.item == "Frasco de estamina":
            self.vida = 25
        elif self.item == "Frasco aumentador de piromancia":
            self.quemado = 3
        elif self.item == "Energizante":
            self.extra_turno = True
        elif self.item == "Capa de Invisibilidad":
            self.invulnerable = True
        elif self.item == "Dureza Extrema":
            self.defensa = True

    def recibir_daño(self, daño):
        if self.invulnerable:
            print(f"🛡️ {self.nombre} evitó el daño con Capa de Invisibilidad!")
            self.invulnerable = False
            return
        if self.defensa:
            daño *= 0.3
            self.defensa = False
        self.vida -= daño
        print(f"💥 {self.nombre} recibe {daño:.1f} de daño. Vida actual: {self.vida:.1f}")

    def atacar(self, objetivo):
        daño = self.daño * 2 if self.furia_activa else self.daño
        print(f"⚔️ {self.nombre} ataca a {objetivo.nombre} con {self.arma}")
        objetivo.recibir_daño(daño)
        self.furia_activa = False


class Juego:
    def __init__(self, personajes):
        self.personajes = personajes

    def elegir_personajes(self):
        print("\n--- Elige 3 personajes por nombre ---")
        for p in self.personajes:
            p.mostrar_stats()

        seleccion = []
        for i in range(3):
            nombre = input(f"Elige personaje {i+1}: ")
            encontrado = next((p for p in self.personajes if p.nombre == nombre), None)
            if encontrado:
                seleccion.append(encontrado)
            else:
                print("Personaje no válido, elige de nuevo.")
                i -= 1
        return seleccion

    def mostrar_equipos(self, equipo_jugador, equipo_cpu):
        print("\n=== Equipo Jugador ===")
        for p in equipo_jugador:
            p.mostrar_stats()
        print("\n=== Equipo CPU ===")
        for p in equipo_cpu:
            p.mostrar_stats()

    def elegir_objetivo(self, equipo):
        print("\nElige el objetivo:")
        for i, p in enumerate(equipo):
            if p.vida > 0:
                print(f"{i+1}. {p.nombre} (Vida: {p.vida:.1f})")
        while True:
            try:
                opcion = int(input("Número del objetivo: ")) - 1
                if 0 <= opcion < len(equipo) and equipo[opcion].vida > 0:
                    return equipo[opcion]
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingresa un número válido.")

    def batalla(self, equipo_jugador, equipo_cpu):
        turno_jugador = True
        todos = equipo_jugador + equipo_cpu

        while any(p.vida > 0 for p in equipo_jugador) and any(p.vida > 0 for p in equipo_cpu):
            print("\n========================")
            self.mostrar_equipos(equipo_jugador, equipo_cpu)
            print("========================")

            if turno_jugador:
                atacante = random.choice([p for p in equipo_jugador if p.vida > 0])
                print(f"\n🎯 Turno del jugador con {atacante.nombre}")
                
                usar_item = input("¿Usar item antes de atacar? (S/N): ").upper()
                if usar_item == "S":
                    atacante.usar_item()

                objetivo = self.elegir_objetivo(equipo_cpu)
                atacante.atacar(objetivo)

                # Si tiene turno extra
                if atacante.extra_turno and objetivo.vida > 0:
                    print(f"🔥 {atacante.nombre} tiene turno extra gracias a Energizante!")
                    objetivo = self.elegir_objetivo(equipo_cpu)
                    atacante.atacar(objetivo)
                    atacante.extra_turno = False

            else:
                atacante = random.choice([p for p in equipo_cpu if p.vida > 0])
                print(f"\n🤖 Turno de la CPU con {atacante.nombre}")
                
                if not atacante.item_usado and random.choice([True, False]):
                    atacante.usar_item()

                objetivo = random.choice([p for p in equipo_jugador if p.vida > 0])
                atacante.atacar(objetivo)

                if atacante.extra_turno and objetivo.vida > 0:
                    print(f"🔥 {atacante.nombre} de la CPU tiene turno extra gracias a Energizante!")
                    objetivo = random.choice([p for p in equipo_jugador if p.vida > 0])
                    atacante.atacar(objetivo)
                    atacante.extra_turno = False

            # Efecto de quemadura
            for p in todos:
                if p.quemado > 0 and p.vida > 0:
                    print(f"🔥 {p.nombre} sufre quemadura")
                    p.recibir_daño(2)
                    p.quemado -= 1

            turno_jugador = not turno_jugador

        if any(p.vida > 0 for p in equipo_jugador):
            print("\n🏆 ¡Ganaste la batalla!")
        else:
            print("\n💀 La CPU ganó la batalla.")


# Crear personajes con VIDA MÁS BAJA
personajes = [
    Jugador("J1", "killer", "Shurikens", 10, "Frasco de furia", 20),
    Jugador("J2", "support", "Bate", 5, "Frasco de estamina", 20),
    Jugador("J3", "piromante", "Magia Oscura", 7, "Frasco aumentador de piromancia", 20),
    Jugador("J4", "selva", "Dagas", 6, "Energizante", 20),
    Jugador("J5", "bandido", "Cuchilla normal", 8, "Capa de Invisibilidad", 20),
    Jugador("J6", "tanque", "Hacha Gigante", 6, "Dureza Extrema", 20)
]

# Iniciar juego
juego = Juego(personajes)
equipo_jugador = juego.elegir_personajes()
equipo_cpu = random.sample([p for p in personajes if p not in equipo_jugador], 3)

juego.batalla(equipo_jugador, equipo_cpu)
