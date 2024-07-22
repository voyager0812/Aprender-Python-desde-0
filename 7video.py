# 7mo video: Sintaxis básica V - Listas

# Se habla sobre las listas:
# Las listas en Python son similares a los arrays, arreglos o vectores en otros lenguajes de programación.
# Una lista puede almacenar varias variables, como si fuera un mueble con múltiples cajones.

# Sintaxis para definir una lista:
nombre_lista = ["elem1", "elem2", "elem3", ...]

# Una lista puede tener de 0 a muchos elementos.
# Los elementos de una lista se enumeran con índices que comienzan desde 0.

# Crear una lista:
mi_lista = ["Pepe", "Pap", "Pipper", "Bob"]

# Imprimir todos los elementos de la lista:
print(mi_lista[:])

# Si quiero traer un dato específico de mi lista, pongo el índice del dato que quiero traer:
# Nota: En el video parece haber un error, los índices en Python empiezan desde 0, así que `mi_lista[4]` daría un error de índice fuera de rango.
# Para llamar a "Bob", se debe usar `mi_lista[3]`:
print(mi_lista[3])  # Esto imprimirá "Bob"

# Se habla de usar índices negativos para acceder a los elementos desde el final de la lista:
print(mi_lista[-2])  # Esto imprimirá "Pipper"

# Se habla de las porciones de lista (slicing) y sus utilidades:
print(mi_lista[1:3])  # Esto imprimirá ['Pap', 'Pipper']
print(mi_lista[2:])   # Esto imprimirá ['Pipper', 'Bob']

# Para agregar un elemento al final de una lista se usa append:
mi_lista.append("Pim")
print(mi_lista)  # Esto imprimirá ['Pepe', 'Pap', 'Pipper', 'Bob', 'Pim']

# Para agregar un elemento en una posición específica se usa insert:
mi_lista.insert(2, "Pim")
print(mi_lista)  # Esto imprimirá ['Pepe', 'Pap', 'Pim', 'Pipper', 'Bob', 'Pim']

# Para agregar múltiples elementos se usa extend:
mi_lista.extend(["Sam", "Basked", "Rim"])
print(mi_lista)  # Esto imprimirá ['Pepe', 'Pap', 'Pim', 'Pipper', 'Bob', 'Pim', 'Sam', 'Basked', 'Rim']

# Se muestra otra función para comprobar si algo está o no está en la lista:
print("Bob" in mi_lista)  # Esto imprimirá True

# Se muestra que las listas pueden almacenar distintos tipos de datos:
mi_lista_mixta = ["Texto", 123, 45.6, True]
print(mi_lista_mixta)  # Esto imprimirá ['Texto', 123, 45.6, True]

# Función para eliminar un elemento específico de la lista:
mi_lista.remove("Pim")
print(mi_lista)  # Esto imprimirá ['Pepe', 'Pap', 'Pipper', 'Bob', 'Pim', 'Sam', 'Basked', 'Rim']

# Función para eliminar el último elemento de la lista:
mi_lista.pop()
print(mi_lista)  # Esto imprimirá ['Pepe', 'Pap', 'Pipper', 'Bob', 'Pim', 'Sam', 'Basked']
