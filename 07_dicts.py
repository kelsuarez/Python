# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

# Es una estructura de datos que permite almacenar pares de datos clave-valor
# Cada elemento dentro de un diccionario consiste en una clave única y su correspondiente valor asociado.
# En lugar de utilizar índices numéricos como en las listas o tuplas, los diccionarios utilizan las claves como identificadores únicos para acceder a los valores asociados. 
# Las claves pueden ser de cualquier tipo inmutable, como cadenas, números o tuplas, mientras que los valores pueden ser de cualquier tipo de dato, incluyendo números, cadenas, listas, tuplas, conjuntos, e incluso otros diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Kelvin", "Apellido": "Suarez", "Edad": 29, 1: "Python"}

my_dict = {
    "Nombre": "Kelvin",
    "Apellido": "Suarez",
    "Edad": 29,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.72
}

print(my_other_dict)
print(my_dict)

# Un len va a indicarme la cantidad de clave:valor que tendo dentro
print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
# La busqueda se realiza por las clave, en ningun caso por el valor
print(my_dict[1])
print(my_dict["Nombre"])

# Me dara falso, mismo si existe porque es el valor
print("Suarez" in my_dict)
# Esta seria la manera correcta, al ser la clave
print("Apellido" in my_dict)

# Inserción

# Para agregar un nuevo campo a nuestro diccionario 
my_dict["Calle"] = "Calle keke"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

# Si quiero eliminar un solo elemento debo pasarle el nombre de la misma
del my_dict["Calle"]
print(my_dict)

# Otras operaciones

# Nos muestra todos las claves con sus respectivos valores que tenemos dentro
print(my_dict.items())
# Nos muestra todas las claves que tengamos dentro
print(my_dict.keys())
# Nos muestra todos los valores que tenemos dentro
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

# Inicialización rápida: Si necesitas crear un diccionario con un conjunto de claves predefinidas, todas con el mismo valor predeterminado, fromkeys() te permite hacerlo de manera más concisa y legible que crear un diccionario vacío y luego asignar valores a cada clave.

# Eficiencia de código: Utilizar fromkeys() puede ser más eficiente en términos de líneas de código y tiempo de ejecución en comparación con la creación manual de un diccionario y la asignación de valores a cada clave, especialmente cuando tienes muchas claves.

# Claves inmutables: Si tienes una secuencia de claves que son inmutables (por ejemplo, cadenas, tuplas, números), fromkeys() proporciona una manera conveniente de inicializar un diccionario sin la necesidad de escribir un bucle para iterar sobre las claves y asignarles un valor.

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "keke")
print((my_new_dict))

my_values = my_new_dict.values() 
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))