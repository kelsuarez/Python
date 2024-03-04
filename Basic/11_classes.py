# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

# Una clase es una plantilla para la creación de objetos. Define las propiedades y comportamientos comunes que tendrán los objetos que se creen a partir de ella. Una clase define el comportamiento de un objeto y los datos que contiene.

# En términos más simples, una clase puede considerarse como un plano o un diseño que describe cómo se deben construir los objetos. Contiene métodos (funciones definidas dentro de la clase) y atributos (variables definidas dentro de la clase) que especifican el comportamiento y las características de los objetos que se instancian a partir de ella.

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Kelvin", "Suarez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Kelvin", "Suarez", "Keke")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)