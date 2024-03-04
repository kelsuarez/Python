# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) # Hacemos una division normal, pero lo aproxima a un numero entero (Flor division)
print(2 ** 3) #  Calcular un exponente
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole

# and (Devulve True si ambos operando son True)
# or (Devuelve True si alguno de los operandos es True)
# not (Devuelve True si algunos de los operandos es Falce)

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) # 3 es mayor que 4 pero al meter el 'not' le pido que me devuelva True