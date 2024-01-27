import random #error de escritura #importa el modulo random
import string #importa los tipos de variables

def generar_contraseña(longitud=8): #hacia falta definir la variable con def #define la funcion
    caracteres = string.ascii_letters + string.digits + string.punctuation #crea la variable y le da un valor
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud)) #crea la variable y le da un valor
    return contraseña #retornar contraseña

print("contraseña_generada: ",generar_contraseña()) #error de escritura. #imprime la contraseña aleatoria
