def calcular_precio_con_descuento(precio_base, porcentaje_descuento):#error de sintaxis,faltaba la definicion de la funcion(def) y dos puntos #define la funcion con dos parametros
    descuento = precio_base * (porcentaje_descuento / 100) #se calcula el descuento
    precio_final = precio_base - descuento #se resta el monto del descuento al precio base
    return precio_final #error de sintaxis #se devuelve el precio final

precio_base = float(input("Ingrese el precio base del producto: ")) #solicita ingresar el precio base, se convierte a decimal
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: ")) #solicita el porcentaje de descuento a aplicar, se convierte a decimal
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento) #llama a la funcion con los valores ingresados, el resultado se le asigna a la variable precio final
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}") #imprime el precio final con el porcentaje de descuento aplicado, utilizando un formato de cadena de f-strings para insertar los valores de salida
