def validar_mensaje(mensaje, palabras_prohibidas):
    for palabra in palabras_prohibidas:
        if palabra in mensaje:
            return False
    return True

mensaje = input("Ingrese su mensaje: ")
palabras_prohibidas = ["prohibido", "inapropiado", "no permitido"]

if validar_mensaje(mensaje, palabras_prohibidas):
    print("Mensaje válido: no contiene palabras prohibidas")
else:
    print("Mensaje no válido: contiene palabras prohibidas")

def validar_sesion(usuario, contraseña):
    if usuario == "admin" and contraseña == "123456":
        return True
    else:
        return False

usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")

if validar_sesion(usuario, contraseña):
    print("Inicio de sesión exitoso")
else:
    print("Error de inicio de sesión")

def validar_contraseña(contraseña, func1, func2):
    return func1(contraseña) and func2(contraseña)

def longitud_valida(cadena):
    return len(cadena) >= 8

def caracteres_especiales(cadena):
    especiales = "!@#$%^&*()-+?_=,<>/"
    return any(char in especiales for char in cadena)

# Validar la contraseña usando las funciones de validación
if validar_contraseña(contraseña, longitud_valida, caracteres_especiales):
    print("Contraseña válida")
else:
    print("Contraseña no válida")
    
    


#Ejercicio 2

