# Definición de la función para contar palabras en un archivo
def contar_palabras_en_archivo(archivo_nombre): #faltaba definir la funcion (def)
    try:
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras) #error de sintaxis
    except FileNotFoundError:
        return f"El archivo {archivo_nombre} no fue encontrado." #error de sintaxis

# Solicitar al usuario que ingrese el nombre del archivo de texto
archivo_nombre = input("Ingrese el nombre del archivo de texto: ") #la variable estaba invertida

# Imprimir el número de palabras en el archivo
print(f"El archivo contiene {contar_palabras_en_archivo(archivo_nombre)} palabras.") #la variable estaba invertida