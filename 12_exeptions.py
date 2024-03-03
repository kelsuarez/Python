# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

# Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal de ejecución. Las excepciones se utilizan para manejar errores y situaciones excepcionales que pueden surgir durante la ejecución de un programa.
# Cuando ocurre una excepción, se genera un objeto de tipo excepción que contiene información sobre el error que ocurrió. Este objeto puede ser "lanzado" (raise) por el código que detecta la excepción, y luego puede ser "capturado" (catch) y manejado por un bloque de código diseñado específicamente para manejar esa excepción.
# En Python, puedes usar bloques try, except, else y finally para manejar excepciones. El bloque try se utiliza para ejecutar un bloque de código donde puede ocurrir una excepción, mientras que el bloque except se utiliza para manejar la excepción si ocurre. El bloque else se ejecuta si no ocurre ninguna excepción en el bloque try, y el bloque finally se ejecuta siempre, independientemente de si ocurre una excepción o no.

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)