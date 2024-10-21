print("")#espacion en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa sirve para Crear un diccionario vacío y lo vaya llenado con información sobre una persona")#imprime el nombre y titulo
print("")#espacio en blanco 
# Crear un diccionario vacío para almacenar la información de la persona
informacion_persona = {}

# Función para añadir datos al diccionario
def añadir_dato(clave, valor):
    informacion_persona[clave] = valor
    # Imprimir el contenido del diccionario después de añadir el dato
    print("Contenido actual del diccionario:")
    for k, v in informacion_persona.items():
        print(f"{k}: {v}")
    print()  # Línea en blanco para mejor legibilidad

# Solicitar información al usuario
nombre = input("Introduce el nombre: ")
añadir_dato("Nombre", nombre)

edad = input("Introduce la edad: ")
añadir_dato("Edad", edad)

sexo = input("Introduce el sexo: ")
añadir_dato("Sexo", sexo)

telefono = input("Introduce el teléfono: ")
añadir_dato("Teléfono", telefono)

correo = input("Introduce el correo electrónico: ")
añadir_dato("Correo Electrónico", correo)

# Imprimir el contenido final del diccionario
print("Información final de la persona:")
for k, v in informacion_persona.items():
    print(f"{k}: {v}")
