### Retos de codigo ###

""""
Escribe un programa que muestre por consola (con un print) 
los numeros de 1 a 100 (ambos incluidos y con un saldo de 
linea entre cada impresion), sustituyendo los siguientes:
    * Multiplos de 3 por la palabra "fizz"
    * Multiplos de 5 por la palabra "buzz"
    * Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz"
"""

"""
def my_program():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

my_program()
"""

my_list = [i + 1 for i in range(100)]
for element in my_list:
    if element % 3 == 0 and element % 5 == 0:
        print("fizzbuzz")
    elif element % 5 == 0:
        print("buzz")
    elif element % 3 == 0:
        print("fizz")
    else:
        print(element)

# ---------------------------------------------------------------------

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS 
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(palabra_one, palabra_two):
    if palabra_one.lower() == palabra_two.lower():
        return False
    return sorted(palabra_one.lower()) == sorted(palabra_two.lower())

print(is_anagram("Amor", "Roma"))

"""
Estoy haciendo un function con 2 parametros.
Tengo una condicion que convierte ambos parametros en miniscula 
y asi compara que no este escrita la misma palabra 2 veces, en ese 
caso me devuelve un False.
Seguido de ello convierto las palabras en miniscula antes de comparar con un sorted
sorted nos devulve una lista, por ende estoy comparando que los caracteres de ambos
son lo mismo
"""

# ---------------------------------------------------------------------

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()

# ---------------------------------------------------------------------

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

es_primo = prime

print(es_primo(5))

for num in range(1, 101):
    if es_primo(num):
        print(num)

"""
def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

is_prime()
"""

# ---------------------------------------------------------------------

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(cadena):
    cadena_invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]
    return cadena_invertida

# Ejemplo de uso
texto = "Me estoy muriendo horrible con todo esto"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)

"""
def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))
"""

# ---------------------------------------------------------------------

"""
CONTANDO PALABRAS
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
Los signos de puntuación no forman parte de la palabra.
Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
No se pueden utilizar funciones propias del lenguaje que
lo resuelvan automáticamente.
"""


text = input("Ingrese una cadena de texto: ")

# Remuevo todos signos
remove = ",;:\n!\"'"
for caracter in remove:
    text = text.replace(caracter,
                        "")
# Convierto el texto en minuscula
text = text.lower()

# Divido una cadena de texto en una lista de palabras utilizando como separador especifico los espacios " "
words = text.split(" ")

# Creo un diccionario vacio 
dictionary_frequency = {}

# Recorro mi lista y actualizo el diccionario para contar la frecuencia de cada palabra
for word in words:
    if word in dictionary_frequency:
        dictionary_frequency[word] += 1
    else:
        dictionary_frequency[word] = 1

for word in dictionary_frequency:
    frequency = dictionary_frequency[word]
    print(f"La palabra '{word}' tiene una frecuencia de {frequency}")
    
    
# ---------------------------------------------------------------------

