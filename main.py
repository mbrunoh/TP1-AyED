import maskpass
from time import sleep
from os import system

ADMIN_USER = "admin"
ADMIN_CONTRASEÑA = "admin"

def login():
   validacion = False
   intento = 0
   while intentos < 3 and validacion == False: 
      user = input('Ingrese nombre de Usuario: ')
      contraseña = maskpass.advpass('Ingrese la Contraseña: ')
      if user != ADMIN_USER or contraseña != ADMIN_CONTRASEÑA:
         intento += 1
         print(f'Nombre de Usuario o contraseña incorrecta ({intento}/3).')
      else:
         validacion = True
   if validacion == False:
      print('Haz alcanzado el limtie de intentos, se cerrara el programa.')
   else:
      print('Gracias por usar nuestro sistema.')
   return validacion

def cartel():
   print("\n....en construcción...")

def mostrar_menu_principal():
   print('---------- MENU PRINCIPAL ----------')
   print("1- Gestion de Aerolineas.")
   print("2- Aprobar/Denegar Promiciones")
   print("3- Gestion de Novedades")
   print("4- Reportes")
   print("0- Salir\n")

def Submenu1():
      print("\n........Gestion de Aerolineas.........")
      print("1- Crear Aerolinea")
      print("2- Modificar Aerolinea")
      print("3- Eliminar Aerolinea")
      print("4- Volver")
      MENU2()


def Submenu2():
      print("\n........Aprobar/Denegar Promociones.........")
      cartel()


def Submenu3():
      print("\n........Gestion de Novedades.........")
      print("1- Crear Novedad")
      print("2- Eliminar Novedad")
      print("3- Ver Novedades")
      print("4- Volver")
      MENU2()


def Submenu4():
      print("\n........Reportes.........")
      print("1- Reporte de Ventas (reservas con estado 'confirmada')")
      print("2- Reporte de Vuelos")
      print("3- Reporte de Usuarios")
      print("4- Volver")
      MENU2()


def MENU2():
   opc2 = 0
   while (opc2 != 4):
      opc2 = int(input(" Ingrese su opcion: "))
      while (opc2 < 1 or opc2 > 4):
         opc2 = int(input("Ingreso Invalido - reintente ... "))
      
      match opc2:
         case 1: cartel()
         case 2: cartel()
         case 3: cartel()
         case 4: print(" \nVolviendo al menú principal...")

def menuAdmin():
   opc = 1
   while (opc != 0 ):
      mostrar_menu_principal()
      opc = int(input("Ingrese su opcion: "))
      match opc:
         case 1: Submenu1()  
         case 2: Submenu2()  
         case 3: Submenu3()  
         case 4: Submenu4()  
         case _: print('Opcion inválida!')


##inicio
def main():
   if login() == True:
      menuAdmin()
main()