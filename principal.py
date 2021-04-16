from contacto import contact
from Lista import list

import Graphic

ListaContactos = list()


def NewContact():

    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    telefono=input("Ingrese Telefono:")

    nContacto=contact(nombre,apellido,telefono)

    if ListaContactos.exist(int(telefono)):
        print()
        print("Error!,el Contacto ya Existe")
        print()
    else:
        ListaContactos.insert(nContacto)
        print("Contacto Agregado Existosamente!")
        print()

def searchContact():
    numero=input("Ingrese el numero a buscar: ")
    if ListaContactos.size()>0:
        if ListaContactos.exist(int(numero))!=True:
            opcion=input("El contacto no Existe,Desea Agregarlo? s/n")

            if opcion == "s":
                NewContact()
        else:
             print()
             print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
             print("Nombre: ",ListaContactos.search(int(numero)).getNombre())
             print("Apellido: ", ListaContactos.search(int(numero)).getApellido())
             print("Telefono: ", ListaContactos.search(int(numero)).getTelefono())
             print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
             print()
def VisulizarAgenda():


    ListaContactos.view()




def menu():


    while True:
        print("1.- Ingresar Nuevo Contacto")
        print("2.- Buscar Contacto")
        print("3.- Visualizar Agenda")
        print("Q para salir")
        print("-----Elija una opcion-----")
        opcion=input()


        if int(opcion) == 1:
            print("Ingrese los datos del Contacto:")
            NewContact()

        elif int(opcion) == 2:
            searchContact()


        elif int(opcion) == 3:
            print("Visualizando Agenda...")
            print("---------------")
            VisulizarAgenda()
            Graphic.grafico(ListaContactos)

            print("---------------")

        elif opcion == 'Q' or opcion =='q':
            break

        else: print("ingrese una opcion valida")

menu()

