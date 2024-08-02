# Crear diccionario para almacenar usuarios y contraseñas
usuarios = {}

def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    # Validar contraseña
    while True:
        contrasena = input(f"Ingrese la contraseña para {nombre}: ")
        if len(contrasena) >= 6 and any(c.isupper() for c in contrasena) \
                and any(c.islower() for c in contrasena) and any(c.isdigit() for c in contrasena) \
                and any(not c.isalnum() for c in contrasena):
            break
        else:
            print("La contraseña debe tener al menos 6 caracteres y contener al menos una mayúscula, una minúscula, un número y un carácter especial.")
    usuarios[nombre] = contrasena

def validar_usuario():
    nombre = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contrasena:
        print("Acceso concedido. ¡Bienvenido!")
    else:
        print("Usuario no válido o contraseña incorrecta.")

# Crear 3 usuarios
for i in range(3):
    crear_usuario()

# Validar usuario
validar_usuario()
