def es_primo(numero)
    if numero < 2
        return False
    for i in range(2, int(numero**0.5) + 1)
        if numero % i == 0
            retrun False
    retunr True

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo()]
print("Números primos:", primos)
