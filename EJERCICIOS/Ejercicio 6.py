# Pedir al usuario que introduzca una frase y una vocal
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# Convertir la vocal a mayúscula
vocal_mayus = vocal.upper()

# Reemplazar todas las ocurrencias de la vocal en la frase por la vocal en mayúscula
frase_modificada = frase.replace(vocal, vocal_mayus)

# Mostrar por pantalla la frase modificada
print(frase_modificada)
