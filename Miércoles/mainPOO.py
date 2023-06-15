from cosas  import Alumno,Perro

def main():

     al1=Alumno("Ruben",20,"ICO")
     print(al1,"\t",vars(al1))
     al1.set_nombre("Manuel")
     #Parte #2
     al1.set_edad(299)
     print(al1)
     al1.esudiar(5)

     #Clase Perro
     perroUno=Perro("Poddle",20,0.35)
     print(f"\n____________Clase Perro______________"
           f"\n{perroUno}\n{vars(perroUno)}")
     perroUno.raza="Otra"
     print(vars(perroUno))
     cachorro=Perro.es_cachorro(perroUno.edad)
     print(cachorro)


main()