#Ejercicio 1 
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo=0):
        self.__numero_cuenta = numero_cuenta  
        self.__saldo = saldo  

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Se depositaron {monto} EU. Saldo actual: {self.__saldo} EU")

    def retirar(self, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            print(f"Se retiraron {monto} EU. Saldo actual: {self.__saldo} EU")
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo} EU")


# Solicitar datos
numero_cuenta = input("Introduce el número de cuenta: ")
saldo_inicial = float(input("Introduce el saldo inicial: "))

cuenta = CuentaBancaria(numero_cuenta, saldo_inicial)

while True:
    print("\nOpciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("Introduce el monto a depositar: "))
        cuenta.depositar(monto)
    elif opcion == "2":
        monto = float(input("Introduce el monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")





# Ejercicio 2 

import math

class Figura:
    def calcular_area(self):
        pass  

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Solicitar datos 
radio = float(input("Introduce el radio del círculo: "))
circulo = Circulo(radio)
print("Área del círculo:", circulo.calcular_area())

lado = float(input("Introduce el lado del cuadrado: "))
cuadrado = Cuadrado(lado)
print("Área del cuadrado:", cuadrado.calcular_area())

base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))
rectangulo = Rectangulo(base, altura)
print("Área del rectángulo:", rectangulo.calcular_area())




# Ejercicio 3 
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if all(casilla == jugador for casilla in tablero[i]) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        mostrar_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0-2): "))
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0-2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("¡Casilla ocupada! Intenta de nuevo.")

if __name__ == "__main__":
    jugar()





