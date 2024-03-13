# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

"""
Es una función que acepta otras funciones como argumentos y/o devuelve una función como resultado.
En otras palabras, una función de orden superior trata a las funciones como ciudadanos de primera clase, lo que significa que las trata como cualquier otro objeto.

Las funciones de orden superior son una parte importante de la programación funcional y proporcionan una forma elegante y poderosa de escribir código más modular, reutilizable y expresivo. Al permitir la composición de funciones y el paso de funciones como argumentos, las funciones de orden superior facilitan la implementación de patrones de diseño como el patrón de estrategia, el patrón de decorador y otros.
"""

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(7))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))