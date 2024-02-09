def es_palindromo(texto): #faltaban dos puntos #define la funcion con el argumento texto
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum()) #transforma las letras en minusculas y elimina los caracteres alfanumericos
    return texto == texto[::-1] #retorna si el texto es igual a texto invertido

palabra_frase = input("Ingrese una palabra o frase: ") #pide a un usuario que ingrese una palabra o frase y le asigna el valor palabara_frase
if es_palindromo(palabra_frase): #faltaba el argumento palabra_frase #verifica si la palabra o frase es un palindromo
    print(f"{palabra_frase} es un palíndromo.") #si es un palindromo muestra que lo es
else:
    print(f"{palabra_frase} no es un palíndromo.") #si no es un palindromo que no lo es
