# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

# La lista sirve para anadir elementos cada uno en una posición (primer elemento 0 | segundo elemento 1 ...)
print(len(my_list))

# Anado elementos a mi lista
my_list = [35, 24, 62, 52, 30, 30, 17]

# Compruebo cuando elementos tengo en mi lista
print(my_list)

# Compruebo la cantidad de elementos que tengo en mi lista
print(len(my_list))

# Anado elementos a mi lista
my_other_list = [29, 1.72, "Kelvin", "Suarez"]

# Compruebo que tipo de dato es (class 'list') para ambos
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])

# El -1 nos lleva al utimo elemento, asimismo -4 nos lleva de nuevo al 1 elemento
print(my_other_list[-1])
print(my_other_list[-4])

# Al count debemos pasarle algo, en este caso 30 (Me devuelve la cantidad de ese elemento que tengo en mi lista (2))
# Sirve para contar cuantas veces se repite
print(my_list.count(30))

# Nos da error porque los elementos [4] o [-5] no existen en nuestra lista
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Kelvin"))

# Si quiero empaquetar una lista ya creada, debo obligatoriamente utilizar la cantidad de elementos que ya tengo dentro
# Usar con cuidado, ya que si adjuntamos algun elemento en nuestra lista original podemos romper todo
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

# Sumo ambas listas
print(my_list + my_other_list)
#print(my_list - my_other_list) error 

# Creación, inserción, actualización y eliminación

# Anadimos un elemento (La operacion .append nos lo coloca al final)
my_other_list.append("Keke")
print(my_other_list)

# Anadimos un elemento (INSERTAMOS) (Nos exige un idice y lo que queremos insertar) (En este caso nos coloca en la posicion 1 "Verde")
my_other_list.insert(1, "Rojo")
print(my_other_list)

# Accedo al valor y lo igualo a un nuevo valor
my_other_list[1] = "Verde"
print(my_other_list)

# Eliminamos un valor de la lista (el primer elemento con ese nombre o valor, en este caso eliminamos "Azul")
# Utilizamos remove para eliminar un elemento que estamos seguros que esta dentro de nuestra lista
my_other_list.remove("Verde")
print(my_other_list)

# Eliminamos en primer 30, asi que nos quedaria en la lista una vez 30
my_list.remove(30)
print(my_list)

# .pop elimina el ultimo elemento por defecto y nos devuelve el elemento eliminado
# Basicamente nos sirve para eliminar y saber cual elemento escogimos
print(my_list.pop())
print(my_list)

# En este caso eliminamos 62 y lo guardamos en una variable que en este caso llamamos my_pop_element
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# Si quiere simplemente eliminar un elemento utilizo directamente del
# del elimina por indice, sin necesidad de saber exactamente su contenido
del my_list[2]
print(my_list)

# Operaciones con listas

# Copiamos nuestra lista (Con su estado actual)
my_new_list = my_list.copy()

# Borramos nuestra lista
my_list.clear()
print(my_list)
print(my_new_list)

# Nos da los valores con el orden inverso 
my_new_list.reverse()
print(my_new_list)

# Ordena nuestra lista (Porque nuestra lista en un int, entonces lo que hace es ponerlos en orden)
# Si fuese una lista con str seria ordenado por orden alfabetico
my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

# Basicamente cambiamos el tipo de nuestra variable y la convertimos en un 'str'
# A TENER EN CUENTA Y CON CUIDADO
my_list = "Hola Python"
print(my_list)
print(type(my_list))