def siguiente(numero):
    return numero + 1

def anterior(numero):
    return numero - 1

def duplicar(numero):
    return numero * 2

def transformar_lista(lista, funcion):
    return [funcion(num) for num in lista]

funciones = {
    "siguiente": siguiente,
    "anterior": anterior,
    "duplicar": duplicar
}

print("Elige una función para transformar la lista:")
print("1 - siguiente")
print("2 - anterior")
print("3 - duplicar")

eleccion = input("Ingresa el número de tu elección: ")

if eleccion == "1":
    funcion_elegida = funciones["siguiente"]
elif eleccion == "2":
    funcion_elegida = funciones["anterior"]
elif eleccion == "3":
    funcion_elegida = funciones["duplicar"]
else:
    print("Elección no válida. Se usará la función 'siguiente' por defecto.")
    funcion_elegida = funciones["siguiente"]

lista_str = input("Ingresa una lista de números separados por comas: ")
lista = [int(num) for num in lista_str.split(",")]
resultado = transformar_lista(lista, funcion_elegida)

print("Lista original:", lista)
print("Lista transformada:", resultado)





#Ejemplo 2 

def siguiente(num):
    return num + 1

def anterior(num):
    return num - 1

def duplicar(num):
    return num * 2

def transformar_lista(lista, funcion):
    return [funcion(x) for x in lista]

entrada = input("Ingresa los números que haran parte de la lista separados por espacios: ")
numeros = list(map(int, entrada.split()))

resultado_siguiente = transformar_lista(numeros, siguiente)
print("Resultado con la función siguiente:", resultado_siguiente)

resultado_anterior = transformar_lista(numeros, anterior)
print("Resultado con la función anterior:", resultado_anterior)

resultado_duplicar = transformar_lista(numeros, duplicar)
print("Resultado con la función duplicar:", resultado_duplicar)
