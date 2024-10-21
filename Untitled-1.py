print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa Hacer un diccionario de traducción español-inglés ")#imprime el nombre del programador y el titulo 
print("")#espacio en blanco 
# Crear un diccionario vacío para almacenar las traducciones
diccionario_traducciones = {}

# Añadir traducciones al diccionario
while True:
    entrada = input("Introduce una traducción en formato 'español:inglés' (o escribe 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    espanol, ingles = entrada.split(':')
    diccionario_traducciones[espanol.strip()] = ingles.strip()

# Solicitar y traducir la frase
frase_espanol = input("Introduce una frase en español para traducir: ")
resultado_traduccion = ' '.joindiccionario_traducciones.get(palabra, palabra) for palabra in frase_es

