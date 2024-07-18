#Ejercicio 1 

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

# ejemplos del ejercicio 1 
banco = Banco("Mi Banco")
cliente1 = Cliente("Pedro")
cliente2 = Cliente("María")
cliente3 = Cliente("Nicolas")

# Agregar clientes al banco
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
banco.adicionar_cliente(cliente3)

# Mostrar el número de clientes
print(f"Clientes en {banco.nombre}: {banco.obtener_numero_clientes()}")



