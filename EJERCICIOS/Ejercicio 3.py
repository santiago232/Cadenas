# Pedir el nombre del usuario
nombre = input("¿Cómo te llamas? ")

# Convertir el nombre a mayúsculas
nombre_mayus = nombre.upper()

# Contar el número de letras del nombre
n = len(nombre)

# Mostrar el resultado por pantalla
print(nombre_mayus + " tiene " + str(n) + " letras")
