import random #error de escritura
import string #importa los tipos de variables

def generar_contraseña(longitud=8): #hacia falta definir la variable con def
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña #retornar contraseña

print("contraseña_generada: ",generar_contraseña()) #error de escritura
