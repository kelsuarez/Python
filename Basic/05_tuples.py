# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

# POR DEFICION UNA TUPLE ES INMUTABLE Y SI LA USAMOS ES PORQUE QUEREMOS VALORES CONSTANTES

# Definimos tuple
my_tuple = tuple()
my_other_tuple = ()

# Asignamos valores a tuple
my_tuple = (29, 1.72, "Kelvin", "Suarez", "Kelvin")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

# Cuenta la cantidad de veces que se encuentra ese elemento
print(my_tuple.count("Kelvin"))
# Nos indica el indice en donde se encuentra ese elemento
print(my_tuple.index("Suarez"))
print(my_tuple.index("Kelvin"))

# No podemos reasignar o adjuntar elementos| SON VALORES CONSTANTES | (tuple no lo soporta, para eso deberiamos usar una lista)
# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

# No podemos modificarlas pero si podemos adjuntarlas 
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

# Buscamos elementos dentro (En este caso seria del elemento 3 al 6)
print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

# Convierto mi tupla en una lista
my_tuple = list(my_tuple)
print(type(my_tuple))

# Inserto elementos a mi lista 
my_tuple[4] = "Keke"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined