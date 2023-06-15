class Alumno:
    facultad="FES Aragon"
    def __init__(self,nombre,edad, carrera):
       # print("Constructor: ", type(self))
        self.__nombre=nombre
        self.__carrera=carrera
        self.__edad=edad
    #Metodos de acceso

    def set_nombre(self,nombre):
        self.__nombre=nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,edad):
        if edad >= 8 and edad <= 70:
          self.__edad=edad
        else:
            print("Edad invalida")

    def get_edad(self):
        return self.__edad

    def set_carrera(self,carrera):
        self.__carrera=carrera

    def get_carrera(self):
        return self.__carrera


    def __str__(self):
        return f"Nombre:{self.__nombre},Edad:{self.__edad},Carrera:{self.__carrera}"

    def esudiar(self,hrs):
        print(f"Alumno:{self.__nombre} Hrs de estudio:{hrs}")


class Perro:

    # Metodo constructor
    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura
    # raza
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    # edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad= edad if edad<=20 else print("Edad invalida")

    # estatura
    @property
    def estarura(self):
     return self.__estatura

    @estarura.setter
    def estatura(self, estatura):
        self.__estatura = estatura if estatura >= 1.1 else print("Estatura invalida")

    def __str__(self):
        return f"Raza:{self.__raza}\t Edad:{self.__edad}\t Estatura:{self.__estatura}"

    # Metodo es cachorro
    @staticmethod
    def es_cachorro(edad):
        return edad <= 3

    # Metodo dormir

    @staticmethod
    def dormir(cls, vueltas):
        for d in range(vueltas):
            print("Revisando el área")

    @classmethod
    def perro_grande(cls, estatura):
      if  estatura > 0.79 : return cls("na", 0, estatura)

