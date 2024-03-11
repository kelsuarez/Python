# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###

# las lambdas son funciones anónimas, lo que significa que son funciones sin nombre. 
# Estas funciones se definen utilizando la palabra clave lambda, seguida de una lista de argumentos, un operador de dos puntos : y una expresión. La expresión es el valor que la función devuelve cuando se llama.

def sum_two_values(
    first_value, second_value): return first_value + second_value


print(sum_two_values(2, 4))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3


print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))