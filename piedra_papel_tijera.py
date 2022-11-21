import random
# ● Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
class Piedra_papel_tijera:
    def __init__(self):
        self.rondas = 0
        self.victoria_maquina = 0
        self.victoria_humano = 0
        self.empate = 0

        
    def nombre(self, nombre):
        nombre = print(f"{nombre} vs Maquina")

    def jugar(self):

        while True:

            jugador_1 = input("Seleccione una de las tres opciónes \nPiedra \nPapel \nTijera\nEscriba opción = ").lower()

            maquina = random.choice(["piedra", "papel", "tijera"])
            self.rondas = self.rondas + 1
            # Primera parte = El jugador elige la opción piedra
            if jugador_1 == "piedra" and maquina == "papel":
                print(f"{nombre} eligio piedra y la maquina eligio papel.\nGanador = Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "tijera":
                print(f"{nombre} eligió piedra y la maquina eligió tijera.\nGanador {nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "piedra":
                print(f"self.empate!!!\nAmbos jugadores elegieron Piedra")
                self.empate = self.empate + 1
            #Segunda parte = el jugador elige la opción ppapel
            elif jugador_1 == "papel" and maquina == "papel":
                print(f"self.empate!!!\nAmbos jugadores elegieron Papel")
                self.empate = self.empate + 1
                print("")
            elif jugador_1 == "papel" and maquina == "tijera":
                print(f"{nombre} eligió papel y la maquina eligió tijera.\nGanador Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            elif jugador_1 == "papel" and maquina == "piedra":
                print(f"El jugdor 1 eligió papel y la maquina eligió piedra.\nGanador {nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")
            #Tercera parte = el jugador elige la opción tijera
            elif jugador_1 == "tijera" and maquina == "tijera":
                print(f"Empate!!!\nAmbos jugadores elegieron Tijera")
                self.empate = self.empate + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "papel":
                print(f"{nombre} eligió tijera y la maquina eligió papel.\nGanador {nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "piedra":
                print(f"El jugdor 1 eligió papel y la maquina eligió piedra.\nGanador Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            # continuar o finalizar
            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break
            print("")
    def resultado(self):
        print(f"Se han jugado un total de {self.rondas} rondas")
        print(f"{nombre} has tenido un total de {self.victoria_humano} partida/s ganadas")
        print(f"La maquina ha obenido un total de  {self.victoria_maquina} partida/s ganadas")
        print(f"Hubo un total de {self.empate} partida/s que terminaron en empates")
        print("")

    def resultado_final(self):
        if self.victoria_humano > self.victoria_maquina and self.victoria_humano > self.empate:
            print(f"{nombre} eres el ganador final!!\nFFELICIDADES!!\nHasta la proxima revancha!!")
        elif self.victoria_maquina > self.victoria_humano and self.victoria_maquina > self.empate:
            print(f"La maquina ha sido el ganador final!!\nHasta la proxima revancha!!!")
        elif self.empate > self.victoria_maquina and self.empate > self.victoria_humano:
            print(f"Se ha producido un self.empate tecnico.\nHasta la proxima revancha!!")
        elif self.victoria_humano == self.empate and self.victoria_maquina == self.empate:
            print("Felicitaciones, has sido el ganado por definición")
        print("")



iniciar = input("Si desea jugar seleccione la letra S caso contrario cualquier letra = ").lower()

if iniciar == "s":
    juego = Piedra_papel_tijera()
    print("Bienvenido al PIEDRA - PAPEL - TIJEA")
    nombre = input("Ingrese su nombre = ")
    juego.nombre(nombre)
    juego.jugar()
    juego.resultado()
    juego.resultado_final()
else:
    print("Hasta luego")

