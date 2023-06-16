from cosas import *

def main():
    per=Persona("Jose",19)
    print(per)
    print(Persona.descripcion)

    print("\n|______________Herencia________________|\n\t_________|Alumno|____________")
    al=Alumno("Jose",19,"256554365","ICO")
    print(al,"\n",Alumno.descripcion,"\n")
    alDos=Alumno.constructor_defecto()
    print(alDos)
    alDos.nombre="Ruben"
    print(alDos)

    print("\n_________|Profesor|_____________")
    prof=Profesor("Jesus",30+16,36365,"Ingenieria de Software")
    print(prof)
    prof.dormir()

    print("\n_________|Ayudante de profesor|_____________")
    ayudante=ayudanteProfesor("Adrian",20,"3249348","ICO",2323,"Ingenieria",5)
    print(ayudante)


main()
