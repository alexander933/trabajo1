def calculadora(): #define la funcion, tipo de dato y variable a ingresar.
    num1 = float(input("Ingrese el primer número: ")) #faltaba el input
    num2 = float(input("Ingrese el segundo número: ")) #faltaba el input
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+': #dependiendo a lo que sea igual operacion hacer un calculo sino es un operador mostrar falla.
        resultado = num1 + num2 #variable incorrecta
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 #variable incorrecta
    else:
        resultado = "Operación no válida"

    print ("Resultado: ", resultado) #faltaba una coma #imprimir el resultado de la operacion

calculadora() #error de escritura #llama la funcion
