# Ejercicio 1 
print(input("Por favor, ingresa un mensaje: ")[::-1].upper())

# Ejercicio 2 
print((lambda m: m[::-1].upper())(''.join(chr((ord(c) - 65 + 3) % 26 + 65) if c.isupper() else chr((ord(c) - 97 + 3) % 26 + 97) if c.islower() else c for c in input("Por favor, ingresa un mensaje: "))))


