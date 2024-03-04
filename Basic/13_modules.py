# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ###

# Un módulo es un archivo que contiene código Python reutilizable. Puede contener definiciones de funciones, clases y variables, así como código ejecutable. Los módulos permiten organizar y reutilizar el código al dividirlo en archivos separados, lo que facilita la mantenibilidad y la reutilización del código.
# Los módulos pueden ser importados en otros programas Python para acceder a las funciones, clases y variables definidas en ellos. Python proporciona una variedad de formas de importar módulos, incluyendo la palabra clave import, la función importlib.import_module() y la sintaxis from ... import .... 

from math import pi as PI_VALUE
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)