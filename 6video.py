# 6to video: Sintaxis básica IV

# Crear una función para combinar 2 valores con el nombre "suma":
def suma():
    num1 = 5
    num2 = 7
    print(num1 + num2)

# Llamada a la función suma:
suma()

# Esto imprimiría en la consola la suma de las 2 variables (num1 y num2).

# Utilidad de reutilizar el código:
# Ejemplo 1: Llamar la función suma() cuantas veces queramos.
suma()
suma()

# Ejemplo 2: Llamar una función que pueda sumar no solo los mismos valores, sino valores distintos.
# ¿Cómo hacer lo segundo? Creando una función que reciba 2 parámetros o 2 argumentos.

# Definir una función con parámetros:
def suma_con_parametros(num1, num2):
    print(num1 + num2)

# Llamar a la función con diferentes valores:
suma_con_parametros(2, 4)  # Esto imprimirá 6
suma_con_parametros(6, 2)  # Esto imprimirá 8

# Profundización en el tema de los parámetros y la reutilización del código.

# Introducción de la función return:
# Comparar con una máquina expendedora de bebidas.

# Función con return:
def suma_con_return(num1, num2):
    resultado = num1 + num2
    return resultado

# Llamada a la función y almacenamiento del resultado:
almacena_resultado = suma_con_return(5, 8)
print(almacena_resultado)  # Esto imprimirá 13

# El valor devuelto por la función se almacena en la variable almacena_resultado y luego se imprime.
