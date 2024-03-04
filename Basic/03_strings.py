# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) #Con len calculamos el numero de letras (incluyendo los espacios)
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" #Con el \n hago un salto de linea, lo ideal seria pegarlos para que no quede un espacio al inicio
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" #Para que comience con una tabulacion 
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" # Para 'escapar' (evitar) que tome en cuenta la tabulacion en este caso, solo hace falta colocar una \ antes
print(my_scape_string)

# Formateo

name, surname, age = "Kelvin", "Suarez", 29
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # Este seria el mejor metodo. Con el podemos evitar que nos introduscan elementos que no queremos, por ejemplo al pedir %d solo podemos recibir numeros.
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Esta manera, aunque es funcional, no es optima

#Inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Esta seria la manera correcta a usar

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

# Estamos escogiendo las letras las detras de la 1 hasta la 3 sin incluir la ultima (en este caso seria la 1 y la 2) es decir 0=P 1=Y 2=T 3=H 4=O 5=N
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) # Nos permite cambiar la primera letra a Mayuscula
print(language.upper()) #  Nos permite cambiar toda la frase a MAYUSCULA 
print(language.count("n")) # Nos cuenta cuantas letras tiene de la letra que queramos
print(language.isnumeric()) # Preguntamos si es un numero
print("1".isnumeric())  # Preguntamos si es un numero
print(language.lower()) # Para cambiar todo a minuscula 
print(language.lower().isupper()) # Se ejecuta la primera que vendria a ser que todo es minuscula y luego en la segunda le preguntamos que si esta en mayuscula, el resultado en este caso es FALSE


print(language.startswith("Py")) # Estamos preguntando si Python empieza con Py, en nuestro caso es falso porque lo tenemos todo en minuscula 
print("Py" == "py")  # No es lo mismo