class Vivienda:
    def __init__(self, nombre, documento_identidad, correo_electronico, numero_celular):
        self.__nombre = nombre
        self.__documento_identidad = documento_identidad
        self.__correo_electronico = correo_electronico
        self.__numero_celular = numero_celular

    def mostrar_informacion(self):
        return (f"Nombre: {self.__nombre}\n"
                f"Documento de Identidad: {self.__documento_identidad}\n"
                f"Correo Electrónico: {self.__correo_electronico}\n"
                f"Número Celular: {self.__numero_celular}")

class Casa(Vivienda):
    def __init__(self, nombre, documento_identidad, correo_electronico, numero_celular,
                 direccion, barrio, localidad, valor_casa):
        super().__init__(nombre, documento_identidad, correo_electronico, numero_celular)
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        self.__valor_casa = self.__validar_valor_casa(valor_casa)
        self.__matricula = 0
        self.__impuesto_predial = 0
        self.__calcular_matricula_e_impuesto()

    def __validar_valor_casa(self, valor_casa):
        while True:
            try:
                valor_casa = float(valor_casa)
                if 300_000_000 <= valor_casa <= 600_000_000:
                    return valor_casa
                else:
                    valor_casa = input("El valor de la casa debe estar entre 300 millones y 600 millones. Inténtelo de nuevo: ")
            except ValueError:
                valor_casa = input("Entrada no válida. Por favor, ingrese un número: ")

    def __calcular_matricula_e_impuesto(self):
        self.__matricula = self.__valor_casa * 0.05
        self.__impuesto_predial = self.__matricula * 0.02

    def mostrar_informacion(self):
        informacion_vivienda = super().mostrar_informacion()
        return (f"{informacion_vivienda}\n"
                f"Dirección: {self.__direccion}\n"
                f"Barrio: {self.__barrio}\n"
                f"Localidad: {self.__localidad}\n"
                f"Valor de la Casa: {self.__valor_casa}\n"
                f"Matrícula: {self.__matricula}\n"
                f"Impuesto Predial: {self.__impuesto_predial}")

class Apartamento(Vivienda):
    def __init__(self, nombre, documento_identidad, correo_electronico, numero_celular,
                 direccion, barrio, localidad, numero_apartamento, bloque_o_interior, piso, valor_apartamento):
        super().__init__(nombre, documento_identidad, correo_electronico, numero_celular)
        self.__direccion = direccion
        self.__barrio = barrio
        self.__localidad = localidad
        self.__numero_apartamento = numero_apartamento
        self.__bloque_o_interior = bloque_o_interior
        self.__piso = piso
        self.__valor_apartamento = valor_apartamento
        self.__impuestos = 0
        self.__calcular_impuestos()

    def __calcular_impuestos(self):
        if self.__piso >= 1 and self.__piso <= 3:
            self.__impuestos = self.__valor_apartamento * 0.03
        elif self.__piso >= 4 and self.__piso <= 8:
            self.__impuestos = self.__valor_apartamento * 0.10
        elif self.__piso >= 9:
            self.__impuestos = self.__valor_apartamento * 0.20

    def mostrar_informacion(self):
        informacion_vivienda = super().mostrar_informacion()
        return (f"{informacion_vivienda}\n"
                f"Dirección: {self.__direccion}\n"
                f"Barrio: {self.__barrio}\n"
                f"Localidad: {self.__localidad}\n"
                f"Número de Apartamento: {self.__numero_apartamento}\n"
                f"Bloque o Interior: {self.__bloque_o_interior}\n"
                f"Piso: {self.__piso}\n"
                f"Valor del Apartamento: {self.__valor_apartamento}\n"
                f"Impuestos: {self.__impuestos}")

def capturar_informacion_vivienda():
    tipo = input("Ingrese el tipo de vivienda (1 para casa / 2 para apartamento): ").strip()

    nombre = input("Ingrese el nombre del comprador: ").strip()
    documento_identidad = input("Ingrese el documento de identidad del comprador: ").strip()
    correo_electronico = input("Ingrese el correo electrónico del comprador: ").strip()
    numero_celular = input("Ingrese el número celular del comprador: ").strip()

    direccion = input("Ingrese la dirección: ").strip()
    barrio = input("Ingrese el barrio: ").strip()
    localidad = input("Ingrese la localidad: ").strip()

    if tipo == "1":
        valor_casa = input("Ingrese el valor de la casa: ").strip().replace(',', '')
        try:
            casa = Casa(nombre, documento_identidad, correo_electronico, numero_celular,
                        direccion, barrio, localidad, valor_casa)
            print("\nInformación de la casa:")
            print(casa.mostrar_informacion())
        except ValueError as e:
            print(f"Error: {e}")
            
    elif tipo == "2":
        numero_apartamento = input("Ingrese el número del apartamento: ").strip()
        bloque_o_interior = input("Ingrese el bloque o interior: ").strip()
        piso = int(input("Ingrese el piso del apartamento: ").strip())
        valor_apartamento = float(input("Ingrese el valor del apartamento: ").strip().replace(',', ''))
        try:
            apartamento = Apartamento(nombre, documento_identidad, correo_electronico, numero_celular,
                                      direccion, barrio, localidad, numero_apartamento, bloque_o_interior, piso, valor_apartamento)
            print("\nInformación del apartamento:")
            print(apartamento.mostrar_informacion())
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Tipo de vivienda no válido. Debe ser '1' para casa o '2' para apartamento.")

def main():
    while True:
        capturar_informacion_vivienda()
        continuar = input("\n¿Desea ingresar otra vivienda? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
