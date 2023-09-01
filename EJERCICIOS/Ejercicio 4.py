# Obtener el número de teléfono con formato prefijo-número-extension
telefono = input("Introduce un número de teléfono con el formato +34-número-extension: ")

# Dividir la cadena por el guión y obtener el segundo elemento de la lista resultante
numero = telefono.split("-")[1]

# Mostrar el número de teléfono sin el prefijo y la extensión
print("El número de teléfono es:", numero)
