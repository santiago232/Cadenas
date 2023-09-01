# Pedir el correo electrónico del usuario
email = input("Introduce tu correo electrónico: ")

# Separar el nombre y el dominio del correo electrónico
nombre, dominio = email.split("@")

# Cambiar el dominio a ceu.es
nuevo_dominio = "ceu.es"

# Concatenar el nombre y el nuevo dominio
nuevo_email = nombre + "@" + nuevo_dominio

# Mostrar el nuevo correo electrónico por pantalla
print("Tu nuevo correo electrónico es: " + nuevo_email)
