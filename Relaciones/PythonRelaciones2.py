# Ejercicio 2 
class Cuenta:
    def __init__(self, id_cuenta, saldo, nombre):
        self.id_cuenta = id_cuenta
        self.saldo = saldo
        self.nombre = nombre

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def ver_info_clientes(self):
        print(f"Clientes del banco {self.nombre}:")
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre}, Cédula: {cliente.cedula}")
            for cuenta in cliente.cuentas:
                print(f"Número de cuenta ({cuenta.nombre}): {cuenta.id_cuenta}, Saldo: {cuenta.saldo}")

    def totalizar_ahorros(self):
        total_ahorros = sum(cuenta.saldo for cliente in self.clientes for cuenta in cliente.cuentas if cuenta.nombre == "ahorros")
        print(f"Total de saldos en cuentas de ahorros: {total_ahorros}")

    def total_saldos_corriente(self):
        total_saldos_corriente = sum(cuenta.saldo for cliente in self.clientes for cuenta in cliente.cuentas if cuenta.nombre == "corriente")
        print(f"Total de saldos en cuentas corrientes: {total_saldos_corriente}")

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.cuentas = []

    def agregar_cuenta(self, id_cuenta, saldo, nombre):
        self.cuentas.append(Cuenta(id_cuenta, saldo, nombre))

# Crear una instancia de Banco
banco = Banco("Mi Banco")

# Crear clientes y cuentas
pedro = Persona("Pedro", "123456")
pedro.agregar_cuenta(1, 1000, "ahorros")
pedro.agregar_cuenta(2, 2000, "corriente")
juan = Persona("Juan", "789012")
juan.agregar_cuenta(3, 1500, "ahorros")
ana = Persona("Ana", "345678")
ana.agregar_cuenta(4, 3000, "corriente")

# Agregar clientes al banco
banco.adicionar_cliente(pedro)
banco.adicionar_cliente(juan)
banco.adicionar_cliente(ana)

# Mostrar información de los clientes
banco.ver_info_clientes()

# Calcular totales
banco.totalizar_ahorros()
banco.total_saldos_corriente()
