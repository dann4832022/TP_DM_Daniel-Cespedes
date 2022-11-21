import random
# ● Adivinar un número compitiendo contra la computadora.
class Adivinar_numeros():
    def __init__(self):
        self.rondas = 0
        self.victoria_maquina = 0
        self.victoria_humano = 0
        self.empate = 0
    
        print("Estamos por jugar")

    def nombre(self, nombre):
        nombre = print(f"{nombre} vs Maquina")

    def jugar(self):
        print("Intente advinar el numero que elegira la maquina.\nTiene que ser un numero del 0 al 10")
        while True:
            jugador_1 = int(input("Ingres el nuemro =  "))
            maquina = random.randint(0, 10)
            print(f"La maquina seleccionó el numero {maquina}")
            self.rondas = self.rondas + 1
            if jugador_1 == maquina:
                print("Has acertado, elegiste el mismo numero que la maquina")
                self.victoria_humano = self.victoria_humano + 1
            else:
                print("Game Over")
                self.victoria_maquina = self.victoria_maquina + 1
            
            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break

    def resultado(self):
        print(f"Se han jugado un total de {self.rondas} rondas")
        print(f"{nombre} has tenido un total de {self.victoria_humano} partida/s ganadas")
        print(f"La maquina ha obenido un total de  {self.victoria_maquina} partida/s ganadas")

        print("")

    def resultado_final(self):
        if self.victoria_humano > self.victoria_maquina:
            print(f"{nombre} eres el ganador final!!\nFFELICIDADES!!\Hasta la proxima revancha!!")
        elif self.victoria_maquina > self.victoria_humano:
            print(f"La maquina ha sido el ganador final!!\nHasta la proxima revancha!!!")

        print("")


iniciar = input("Si desea jugar seleccione la letra S caso contrario cualquier letra = ").lower()

if iniciar == "s":
    juego = Adivinar_numeros()
    print("Bienvenido al Adivine el numero")
    nombre = input("Ingrese su nombre = ")
    juego.nombre(nombre)
    juego.jugar()
    juego.resultado()
    juego.resultado_final()
else:
    print("Hasta luego")