# VARIABLES
# Todas las variables se escriben en minuscula 

my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_variable, my_int_variable, my_bool_variable)
# Si le coloco una , puedo adjuntar varias variables en una sola 

my_int_str_variable = str(my_int_variable)
print(my_int_str_variable)
print(type(my_int_str_variable))
# Al utilizar un str convertimos la variable my_int_variable que era un numero 5 en string

print(type(print(my_int_str_variable)))
# Al hacer esto rompemos 

# FUNCIONES DEL SISTEMA

print(len(my_int_str_variable))
# Cuenta el numero de caracteres que contiene la variable, en este caso como es un numero me da como resultado 1

# VARIABLES EN UNA SOLA LINEA (NO AABUSAR DE LA SINTAXIS)
name, surname, alias, age = "Kelvin", "Suarez", "kel", 28
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es: ", alias)

# INPUTS 
# Con los inputs podemos imprimir directamente desde la terminal, es decir, segun el elemento que le asignemos a la pregunta obtendremos un resultado
"""
first_name =  input('Cual es tu nombre?: ')
my_age = input('Que edad tienes?: ')

print(first_name)
print(my_age)
"""
#En este caso, pedimos une informacion y luego imprimimos la respuesta 