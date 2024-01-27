def contar_palabra(texto, palabra): #define la función #hacia falta los dos puntos
    return texto.lower().split().count(palabra.lower()) #Convierte todo el texto a minúsculas,Divide el texto en palabras, creando una lista de palabras,Cuenta cuántas veces aparece la palabra (convertida a minúsculas) en la lista de palabras.

texto = "Este es un ejemplo de texto Este texto tiene palabras repetidas." #sobraba un punto #crea una variable llamada texto y le asigna un valor
palabra_buscada = "texto" #crea una variable llamada palabra_buscada y le asigna un valor.

print(f"La palabra '{palabra_buscada} aparece {contar_palabra(texto, palabra_buscada)} veces.")#hacia falta un corchete #imprime las veces que se repite la palabra.
