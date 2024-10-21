print("")#imprime espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196  este programa  Hace un diccionario de traducción español-inglés") #imprime nombre y titulo
print("")#imprime espacio en blanco

def crear_diccionario(pares):
    diccionario = {}
    for par in pares.split(","):
        palabra, traduccion = par.split(":")
        diccionario[palabra.strip()] = traduccion.strip()
    return diccionario

def traducir_frase(frase, diccionario):
    palabras = frase.split()
    traduccion = ""
    for palabra in palabras:
        if palabra in diccionario:
            traduccion += diccionario[palabra] + " "
        else:
            traduccion += palabra + " "
    return traduccion.strip()

# Introducir las palabras en español e inglés separadas por dos puntos y cada par separado por comas
pares = "hola:hello,adios:goodbye,casa:house,perro:dog,gato:cat"

# Crear el diccionario
diccionario = crear_diccionario(pares)

# Pedir al usuario que introduzca una frase en español
frase_espanol = input("Por favor, introduce una frase en español: ")

# Traducir la frase palabra por palabra utilizando el diccionario
frase_traducida = traducir_frase(frase_espanol, diccionario)

print("La traducción de la frase es: ", frase_traducida)