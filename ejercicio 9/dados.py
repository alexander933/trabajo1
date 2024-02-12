import random #error de sintaxtis #importa el modulo random

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado): #faltaba definir la funcion(def) y dos puntos #define la funcion y toma dos argumentos
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)] #se genera una lista llamada resultados, que contiene los resultados de la tirada de los dados
    return resultados #error de sintaxis #la funcion devuelve el resultado de la tirada de los dados

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: ")) #solicita ingresar la cantidad de dados y convierte la  cifra a entero
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: ")) #solicita ingresar la cantidad de caras por dado y convierte la cifra a entero
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado) #faltaba un argumento #se llama la funcion con los valores ingresados, el resultado se guarda en lanzammientos
print(f"Resultados del lanzamiento: {lanzamientos}") #se imprime en pantalla en resultado del lanzamiento de los dados, utilizando una cadena formateada donde lanzamientos se sustituye por el resultado de la funcion
