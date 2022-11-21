import random
class Tirar_dados():

    def __init__(self):
      
        self.dado_1 = 0
        self.dado_2 = 0
        self.numero_minimo = 1
        self.numero_maximo = 6
        self.rondas = 0
        self.victorias = 0
        self.perdida = 0

    def nombre(self,nombre):
        nombre = print(f"{nombre} vs Maquina")

    
    def jugar(self):
        while True:
            tirar_dados = input("Deseas tirar los dados SI/NO == ")
            self.dado_1 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_1)
            self.dado_2 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_2)
            self.rondas = self.rondas + 1
            if self.dado_1 == self.dado_2:
                print("Los numeros de ambos dados son iguales.\nFelicidades.\nHas ganado la partida")
                self.victorias = self.victorias + 1
            else:
                print("No coincidien los numeros.\nHas perdido la partida.")
                self.perdida = self.perdida + 1
            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break

    def puntajes(self):
        print(f"Se han judado un total de {self.rondas}")
        print(f"{nombre} Has ganado un total de {self.victorias} partidas!!..")
        print(f"{nombre} Has perdido un total de {self.perdida} partidas!!..")

    def resultado_final(self):
        if self.victorias > self.perdida:
            print(f"Eres el ganador final del juego")
        elif self.victorias < self.perdida:
            print(f"Has perdido mas veces de las que has ganado. Sigue intentando")
        elif self.victorias == self.perdida:
            print("Se ha producido un empate, has ganado y perdido las mismmas cantidad de veces.\nAimate a la revancha")
iniciar = input("Si desea jugar seleccione la letra S caso contrario cualquier letra = ").lower()

if iniciar == "s":
    juego = Tirar_dados()
    print("Bienvenido la tira de de dados")
    nombre = input("Ingrese su nombre = ")
    juego.nombre(nombre)
    juego.jugar()
    juego.puntajes()
    juego.resultado_final()
else:
    print("Hasta luego")

