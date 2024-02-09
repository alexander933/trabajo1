def celsius_a_fahrenheit(celsius): #faltaban los dos puntos  #define la funcion
    return (celsius * 9/5) + 32   #faltaba un más  #el resultado de la operacion es el resultado de la funcion

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: ")) #faltaba un input #ingresar la temperatura,el valor convertido en punto flotante se le asigna a la variable
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius) #calcula la temperatura equivalente en fahrenheit
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F") #imprime la temperatura
