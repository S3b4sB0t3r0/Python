from abc import ABC, abstractmethod

class Vivienda(ABC):
    def __init__(self, nombre, documento, correo, celular):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.celular = celular

    @abstractmethod
    def venta(self):
        pass

class Casa(Vivienda):
    def __init__(self, nombre, documento, correo, celular, direccion, barrio, localidad, valor_casa):
        super().__init__(nombre, documento, correo, celular)
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        if valor_casa <= 0:
            raise ValueError("El valor de la casa debe ser positivo")
        self.__valor_casa = valor_casa
        self.__matricula = 0
        self.__impuesto_predial = 0
        self.calcular_valor_a_pagar()

    def calcular_valor_a_pagar(self):
        if 300_000_000 <= self.__valor_casa <= 600_000_000:
            self.__matricula = 0.05 * self.__valor_casa
            self.__impuesto_predial = 0.02 * self.__matricula
        else:
            raise ValueError("El valor de la casa debe estar entre 300 y 600 millones")

    def venta(self):
        return {
            'Nombre': self.nombre,
            'Documento': self.documento,
            'Correo': self.correo,
            'Celular': self.celular,
            'Dirección': self.__direccion,
            'Barrio': self.__barrio,
            'Localidad': self.__localidad,
            'Valor de la Casa': self.__valor_casa,
            'Matrícula': self.__matricula,
            'Impuesto Predial': self.__impuesto_predial
        }

class Apartamento(Vivienda):
    def __init__(self, nombre, documento, correo, celular, numero_apartamento, bloque_interior, piso, valor_apartamento):
        super().__init__(nombre, documento, correo, celular)
        if piso <= 0:
            raise ValueError("El piso debe ser un número positivo")
        if valor_apartamento <= 0:
            raise ValueError("El valor del apartamento debe ser positivo")
        self.__numero_apartamento = numero_apartamento
        self.__bloque_interior = bloque_interior
        self.__piso = piso
        self.__valor_apartamento = valor_apartamento
        self.__impuesto = 0
        self.calcular_impuesto()

    def calcular_impuesto(self):
        if 1 <= self.__piso <= 3:
            self.__impuesto = 0.03 * self.__valor_apartamento
        elif 4 <= self.__piso <= 8:
            self.__impuesto = 0.10 * self.__valor_apartamento
        elif self.__piso >= 9:
            self.__impuesto = 0.20 * self.__valor_apartamento
        else:
            raise ValueError("El piso debe ser un número positivo")

    def venta(self):
        return {
            'Nombre': self.nombre,
            'Documento': self.documento,
            'Correo': self.correo,
            'Celular': self.celular,
            'Número de Apartamento': self.__numero_apartamento,
            'Bloque/Interior': self.__bloque_interior,
            'Piso': self.__piso,
            'Valor del Apartamento': self.__valor_apartamento,
            'Impuesto': self.__impuesto
        }

def main():
    viviendas = []

    while True:
        tipo_input = input("Seleccione el tipo de vivienda (1 para Casa, 2 para Apartamento) o 'fin' para terminar: ").strip().lower()
        
        if tipo_input == 'fin':
            break

        if tipo_input == '1':
            tipo = 'casa'
        elif tipo_input == '2':
            tipo = 'apartamento'
        else:
            print("Selección no válida. Ingrese 1 para Casa o 2 para Apartamento.")
            continue

        nombre = input("Ingrese el nombre del comprador: ")
        documento = input("Ingrese el documento de identidad: ")
        correo = input("Ingrese el correo electrónico: ")
        celular = input("Ingrese el número de celular: ")
        
        if tipo == 'casa':
            direccion = input("Ingrese la dirección de la casa: ")
            barrio = input("Ingrese el barrio: ")
            localidad = input("Ingrese la localidad: ")
            while True:
                try:
                    valor_casa = float(input("Ingrese el valor de la casa (en millones): ")) * 1_000_000
                    if valor_casa <= 0:
                        raise ValueError("El valor de la casa debe ser positivo")
                    casa = Casa(nombre, documento, correo, celular, direccion, barrio, localidad, valor_casa)
                    viviendas.append(casa)
                    break
                except ValueError as e:
                    print(e)
                    print("Por favor, ingrese un valor válido para la casa en el rango de 300 a 600 millones.")
        
        elif tipo == 'apartamento':
            while True:
                try:
                    numero_apartamento = int(input("Ingrese el número de apartamento: "))
                    if numero_apartamento <= 0:
                        raise ValueError("El número de apartamento debe ser positivo")
                    break
                except ValueError as e:
                    print(e)
                    print("Por favor, ingrese un número válido para el apartamento.")
            
            bloque_interior = input("Ingrese el bloque o interior: ")
            
            while True:
                try:
                    piso = int(input("Ingrese el piso del apartamento: "))
                    if piso <= 0:
                        raise ValueError("El piso debe ser un número positivo")
                    break
                except ValueError as e:
                    print(e)
                    print("Por favor, ingrese un número válido para el piso del apartamento.")
            
            while True:
                try:
                    valor_apartamento = float(input("Ingrese el valor del apartamento (en millones): ")) * 1_000_000
                    if valor_apartamento <= 0:
                        raise ValueError("El valor del apartamento debe ser positivo")
                    apartamento = Apartamento(nombre, documento, correo, celular, numero_apartamento, bloque_interior, piso, valor_apartamento)
                    viviendas.append(apartamento)
                    break
                except ValueError as e:
                    print(e)
                    print("Por favor, ingrese un valor válido para el apartamento en millones.")
        
        else:
            print("Tipo de vivienda no reconocido. Por favor ingrese '1' para Casa o '2' para Apartamento.")
    
    print("\nResumen de las viviendas:")
    for vivienda in viviendas:
        print(vivienda.venta())

if __name__ == "__main__":
    main()
