class Persona:
    def __init__(self, nombre, documento, direccion):
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_direccion(direccion)

    # get y set de persona
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

# Clase Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, documento, direccion, codigo, programa, trimestre):
        super().__init__(nombre, documento, direccion)
        self.set_codigo(codigo)
        self.set_programa(programa)
        self.set_trimestre(trimestre)

    # get y set de estudiante
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        self.__programa = programa

    def get_trimestre(self):
        return self.__trimestre

    def set_trimestre(self, trimestre):
        self.__trimestre = trimestre

    # Mostrar datos estudiante
    def mostrar_datos(self):
        return (f'Nombre: {self.get_nombre()}\n'
                f'Documento: {self.get_documento()}\n'
                f'Dirección: {self.get_direccion()}\n'
                f'Código: {self.get_codigo()}\n'
                f'Programa: {self.get_programa()}\n'
                f'Trimestre: {self.get_trimestre()}')

# Clase Empleado
class Empleado(Persona):
    def __init__(self, nombre, documento, direccion, codigo, cargo, empresa, sueldo):
        super().__init__(nombre, documento, direccion)
        self.set_codigo(codigo)
        self.set_cargo(cargo)
        self.set_empresa(empresa)
        self.set_sueldo(sueldo)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    # Mostrar datos empleado
    def mostrar_datos(self):
        return (f'Nombre: {self.get_nombre()}\n'
                f'Documento: {self.get_documento()}\n'
                f'Dirección: {self.get_direccion()}\n'
                f'Código: {self.get_codigo()}\n'
                f'Cargo: {self.get_cargo()}\n'
                f'Empresa: {self.get_empresa()}\n'
                f'Sueldo: {self.get_sueldo()}')

#####################################################
# Insertar datos en estudiante
def recoger_datos_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    documento = input("Ingrese el documento del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    codigo = input("Ingrese el código del estudiante: ")
    programa = input("Ingrese el programa del estudiante: ")
    trimestre = input("Ingrese el trimestre del estudiante: ")
    estudiante = Estudiante(nombre, documento, direccion, codigo, programa, trimestre)
    return estudiante

# Insertar datos en empleado
def recoger_datos_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    documento = input("Ingrese el documento del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    codigo = input("Ingrese el código del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    empresa = input("Ingrese la empresa del empleado: ")
    sueldo = input("Ingrese el sueldo del empleado: ")
    empleado = Empleado(nombre, documento, direccion, codigo, cargo, empresa, sueldo)
    return empleado

def main():
    estudiantes = []
    empleados = []
    
    while True:
        tipo = input("¿Qué tipo de persona desea ingresar? (estudiante/empleado) o 'salir' para terminar: ").strip().lower()
        
        if tipo == 'estudiante':
            estudiante = recoger_datos_estudiante()
            estudiantes.append(estudiante)
            print("Datos del estudiante ingresados con éxito.")
        
        elif tipo == 'empleado':
            empleado = recoger_datos_empleado()
            empleados.append(empleado)
            print("Datos del empleado ingresados con éxito.")
        
        elif tipo == 'salir':
            break
        
        else:
            print("Opción no válida. Por favor, ingrese 'estudiante', 'empleado' o 'salir'.")
    
    print("\nDatos de Estudiantes:")
    for estudiante in estudiantes:
        print(estudiante.mostrar_datos())
    
    print("\nDatos de Empleados:")
    for empleado in empleados:
        print(empleado.mostrar_datos())

if __name__ == "__main__":
    main()

