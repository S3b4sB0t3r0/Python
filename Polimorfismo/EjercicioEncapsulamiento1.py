# ejemplo 1 

class Banco:
    def __init__(self, nombre, celular, cuenta, direccion, email, saldo):
        self.set_nombre(nombre)
        self.set_celular(celular)
        self.set_numerocuenta(cuenta)
        self.set_direccion(direccion)
        self.set_email(email)
        self.set_saldo(saldo)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_celular(self, celular):
        self.__celular = celular

    def get_celular(self):
        return self.__celular

    def set_numerocuenta(self, cuenta):
        self.__numerocuenta = cuenta

    def get_numerocuenta(self):
        return self.__numerocuenta

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_direccion(self):
        return self.__direccion

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

# Solicitar datos
nombre = input("Ingrese el nombre del cliente: ")
celular = int(input("Ingrese el número de celular: "))
cuenta = int(input("Ingrese el número de cuenta: "))
direccion = input("Ingrese la dirección: ")
email = input("Ingrese el correo electrónico: ")
saldo = float(input("Ingrese el saldo inicial: "))


cliente = Banco(nombre, celular, cuenta, direccion, email, saldo)

# Mostrar información
print(f"El número de cuenta es {cliente.get_numerocuenta()} del usuario {cliente.get_nombre()}.")
print(f"Su número de celular es {cliente.get_celular()} y su dirección es {cliente.get_direccion()}.")
print(f"Su correo electrónico es {cliente.get_email()} y el saldo es de ${cliente.get_saldo():,.2f}.")

