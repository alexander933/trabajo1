def es_primo(numero): #faltaban dos puntos #se define la funcion, con un numero como argumento
    if numero < 2: #faltaban dos puntos #se verifica si el numero es menor que 2 
        return False #si, si se devuelve porque los menores que 2 no son primos
    for i in range(2, int(numero**0.5) + 1): #faltaban dos puntos #comprueba si el numero es divisible por algun numero en elm rango.
        if numero % i == 0: #faltaban dos puntos
            return False #error de sintaxis #si es divisible devolverse pues no es primo
    return True #error de sintaxis #si no es divisible seguir

limite = int(input("Ingrese el límite superior para encontrar números primos: ")) #ingresar el rango
primos = [num for num in range(2, limite + 1) if es_primo(num)] #faltaba poner num # genera todos los numeros primos desde 2 hasta el rango, utlizando la funcion es_primo
print("Números primos:", primos) #imprime los numeros primos
