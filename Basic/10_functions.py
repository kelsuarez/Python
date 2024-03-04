# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos

# De nada sirve colocarle que sea int o str porque al final el tipado es debil 
def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

# Debo crear una variable si quiero poder utilisarlo
my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")

# Puedo cambiar el orden, pero siempre tomando en cuenta la cantidad de parametros que hay
print_name(surname="Kelvin", name="Suarez")

# Función con parámetros de entrada/argumentos por defecto

# Defino directamente que debe imprimir en caso de que el usuario no coloque nada (sin alias)
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Suarez", "Kelvin")
print_name_with_default("Suarez", "Kelvin", "Keke")




# Función con parámetros de entrada/argumentos arbitrarios

# Al colocar el * me permite de pasar el numero de datos que yo necesite
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Keke")
print_upper_texts("Hola")