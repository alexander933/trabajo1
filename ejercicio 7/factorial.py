def factorial(n): #faltaban dos puntos #define la funcion factorial con el argumento n
    if n == 0 or n == 1: #faltaba un igual y dos puntos #comprueba si n es igual a 0 o 1, el factorial es 1
        return 1 #error de sintaxis #retorna 1
    else:
        return n * factorial(n - 1) #error de sintaxis #si no es igual, calcula el factorial y retorna n multiplicado por el factorial n-1

numero = int(input("Ingrese un número para calcular su factorial: ")) # solicita el ingreso de un numero y lo convierte en entero
print(f"El factorial de {numero} es {factorial(numero)()}") #faltaba pasar numero como argumento a factorial #imprime el calculo
