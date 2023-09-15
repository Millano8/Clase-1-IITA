"""
# Functional Programming

- Realizar un programa que, a su criterio, es m s adecuado para ser resuelto con programaci n funcional.
- El programa debe tener al menos 3 funciones. Una de cada tipo: map, reduce, filter
"""

# Programa para dada una lista de numeros, me devuelva numeros multiplicados x2, los numeros pares y la suma total:

from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para multiplicar un número por 2
def multiplicar_por_dos(x):
    return x * 2

# Función para verificar si un número es par
def es_par(x):
    return x % 2 == 0

# Utilizar map para multiplicar cada número por 2
numeros_multiplicados = list(map(multiplicar_por_dos, numeros))

# Utilizar filter para obtener solo los números pares
numeros_pares = list(filter(es_par, numeros))

# Utilizar reduce para sumar todos los números
suma_total = reduce(sumar, numeros)

# Imprimir resultados
print("Números multiplicados por 2:", numeros_multiplicados)
print("Números pares:", numeros_pares)
print("Suma total de los números:", suma_total)
