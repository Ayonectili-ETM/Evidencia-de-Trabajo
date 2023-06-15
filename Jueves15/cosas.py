#____________________Clase jueves___________
#Clase autor
class Autor:

    #Metodo constructor
    def __init__(self,nombre,pseudo):
        self.__nombre=nombre
        self.__pseudo=pseudo
    #Metodos Getter y setter para la clase autor
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def pseudo(self):
        return self.__nombre
    @pseudo.setter
    def pseudo(self, pseudo):
        self.__pseudo =pseudo

    def __str__(self):
        return f"nombre: {self.__nombre} pseudonimo: {self.__pseudo}"

    def escribir(self):
        print(f" {self.__pseudo} está escribiendo su siguiente : ")


#Clase libro
class Libro:

    # Metodo constructor
     def __init__(self,titulo,autor,an,editorial):
         self.__titulo=titulo
         self.__autor=autor
         self.__an=an
         self.__editorial=editorial

     @property
     def titulo(self):
        return self.__titulo

     @titulo.setter
     def titulo(self,titulo):
        self.__titulo=titulo
    #Autor

     @property
     def Autor(self):
        return self.__autor


     @Autor.setter
     def Autor(self, autor):
        self.__autor =autor
    #Años
     @property
     def an(self):
        return self.__an


     @an.setter
     def an(self, an):
        self.__an =an
#Editorial

     @property
     def editorial(self):
        return self.__editorial

     @editorial.setter
     def editorial(self, editorial):
        self.__editorial = editorial
     def __str__(self):
         return f"Titulo: {self.__titulo}\nAutor: {self.__autor}\nEditorial: {self.__editorial}"
     @classmethod
     def libro_planeta(cls,titulo,autor,ans):
        return cls(titulo,autor,ans,"Planeta")

     def leer(self,minutos):
         print(f"Leyendo por {minutos} minutos")
#Ejercicio Dos
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    #Metodos Getter y Setter
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,cambio):
        self.__nombre=cambio

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, cambio):
        self.__edad = cambio


class Alumno(Persona):
    #Metodo constructor
    def __init__(self,nombre,edad,numero_cuenta,carrera,promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta=numero_cuenta
        self.__carrea=carrera
        self.__promedio=promedio

     #Metodos Getter y setter
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    @numero_cuenta.setter
    def numero_cuenta(self,cambio):
        self.__numero_cuenta=cambio

    @property
    def carrera(self):
        return self.__carrea
    @numero_cuenta.setter
    def carrera(self, cambio):
        self.__carrea = cambio

    @property
    def promedio(self):
        return self.__promedio
    @numero_cuenta.setter
    def promedio(self, cambio):
        self.__promedio = cambio

    def __str__(self):
        return f"Nombre:{self.nombre}\nEdad: {self.edad}\nNumero de cuenta:{self.__numero_cuenta}\n" \
               f"Carrera: {self.__carrea}\nPromedio: {self.__promedio} "