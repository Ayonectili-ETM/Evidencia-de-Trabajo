from cosas import *

def main():
     l1=Libro.libro_planeta("El perfume",Autor("Patrik"," PS"),1980)
     print(f"\n____________Libro_______________\n\n{l1}")
     print(l1)
     #Cambio de pseudonimo a letras minusculas
     l1.Autor.pseudo=l1.Autor.pseudo.lower()
     print("\nCambio a minusculas:", l1)
     al2= Alumno("Jose",19,"114005265","ICO",9.8)
     print(f"\n____________Estudiante_______________\n\n{al2}")

main()