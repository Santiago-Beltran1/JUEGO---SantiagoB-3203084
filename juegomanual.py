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

    def elegir_personajes(self, jugador_num):
        print(f"\n--- Jugador {jugador_num}, elige 3 personajes por nombre ---")
        for p in self.personajes:
            p.mostrar_stats()

        seleccion = []
        while len(seleccion) < 3:
            nombre = input(f"Elige personaje {len(seleccion)+1}: ")
            encontrado = next((p for p in self.personajes if p.nombre == nombre and p not in seleccion), None)
            if encontrado:
                seleccion.append(encontrado)
            else:
                print("Personaje no válido o ya elegido, intenta de nuevo.")
        return seleccion

    def mostrar_equipos(self, equipo1, equipo2):
        print("\n=== Equipo Jugador 1 ===")
        for p in equipo1:
            p.mostrar_stats()
        print("\n=== Equipo Jugador 2 ===")
        for p in equipo2:
            p.mostrar_stats()

    def elegir_objetivo(self, equipo):
        print("\nElige el objetivo:")
        vivos = [p for p in equipo if p.vida > 0]
        for i, p in enumerate(vivos):
            print(f"{i+1}. {p.nombre} (Vida: {p.vida:.1f})")
        while True:
            try:
                opcion = int(input("Número del objetivo: ")) - 1
                if 0 <= opcion < len(vivos):
                    return vivos[opcion]
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Ingresa un número válido.")

    def batalla(self, equipo1, equipo2):
        turno_jugador1 = True
        todos = equipo1 + equipo2

        while any(p.vida > 0 for p in equipo1) and any(p.vida > 0 for p in equipo2):
            print("\n========================")
            self.mostrar_equipos(equipo1, equipo2)
            print("========================")

            if turno_jugador1:
                print("\n🎯 Turno del Jugador 1")
                equipo_atacante, equipo_oponente = equipo1, equipo2
            else:
                print("\n🎯 Turno del Jugador 2")
                equipo_atacante, equipo_oponente = equipo2, equipo1

            atacante = self.elegir_objetivo(equipo_atacante)
            usar_item = input(f"¿{atacante.nombre} usa item antes de atacar? (S/N): ").upper()
            if usar_item == "S":
                atacante.usar_item()

            objetivo = self.elegir_objetivo(equipo_oponente)
            atacante.atacar(objetivo)

            if atacante.extra_turno and objetivo.vida > 0:
                print(f"🔥 {atacante.nombre} tiene turno extra gracias a Energizante!")
                objetivo = self.elegir_objetivo(equipo_oponente)
                atacante.atacar(objetivo)
                atacante.extra_turno = False

            # Daño por quemadura
            for p in todos:
                if p.quemado > 0 and p.vida > 0:
                    print(f"🔥 {p.nombre} sufre quemadura")
                    p.recibir_daño(2)
                    p.quemado -= 1

            turno_jugador1 = not turno_jugador1

        if any(p.vida > 0 for p in equipo1):
            print("\n🏆 ¡Jugador 1 gana la batalla!")
        else:
            print("\n🏆 ¡Jugador 2 gana la batalla!")


personajes = [
    Jugador("J1", "killer", "Shurikens", 10, "Frasco de furia", 20),
    Jugador("J2", "support", "Bate", 5, "Frasco de estamina", 20),
    Jugador("J3", "piromante", "Magia Oscura", 7, "Frasco aumentador de piromancia", 20),
    Jugador("J4", "selva", "Dagas", 6, "Energizante", 20),
    Jugador("J5", "bandido", "Cuchilla normal", 8, "Capa de Invisibilidad", 20),
    Jugador("J6", "tanque", "Hacha Gigante", 6, "Dureza Extrema", 20)
]

# Iniciar juego para 2 jugadores
juego = Juego(personajes)
equipo1 = juego.elegir_personajes(1)
equipo2 = juego.elegir_personajes(2)
juego.batalla(equipo1, equipo2)
