# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

# set es un tipo de dato
# Es una estructura de datos que representa una colección desordenada de elementos únicos. 
# Esto significa que un conjunto no puede contener elementos duplicados y, a diferencia de las listas o tuplas, no tiene un orden definido. 
# Los set son útiles cuando necesitas almacenar elementos únicos y realizar operaciones como unión, intersección y diferencia entre conjuntos.

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Kelvin", "Suarez", 29}
print(type(my_other_set))

# Contamos la cantidad de datos que tenemos dentro (3)
print(len(my_other_set))

# Inserción

# Con add adjuntamos un elemento nuevo a nuestro set
my_other_set.add("Keke")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Keke")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

# Con esto estoy comprobando si el dato existe en nuestro set
print("Suarez" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

# Elimino un elemento dentro de mi set
my_other_set.remove("Suarez")
print(my_other_set)

# Vacio todos los elementos, pero el set sigue creado
my_other_set.clear()
print(len(my_other_set))

# Elimino directamente todo el set con sus elementos
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

# Hacer esto es erreneo y arriesgado, porque siempre aparecera un dato en aleatorio 
my_set = {"Suarez", "Kelvin", 29}
my_list = list(my_set)
print(my_list)
print(my_list[0])


my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

# Para unir dos set
my_new_set = my_set.union(my_other_set)
# En los 2 primeros union no pasa nada, porque no estoy agregando nuevos elementos, y un set no repite.
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

# Imprimimos la diferencia entre my_new_set y my_set | Al haber hecho solo un print en la anterior, no tenemos en una variable los elementos JavaScript C#
print(my_new_set.difference(my_set))