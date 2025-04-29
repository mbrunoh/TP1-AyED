import maskpass
from time import sleep
from os import system

ADMIN_USER = "admin"
ADMIN_CONTRASENA = "admin"

def login():
   validacion = False
   intentos = 0
   while intentos < 3 and validacion == False: 
      user = input('Ingrese nombre de Usuario: ')
      contrasena = maskpass.advpass('Ingrese la Contraseña: ')
      if user != ADMIN_USER or contrasena != ADMIN_CONTRASENA:
         intentos += 1
         print(f'Nombre de Usuario o contraseña incorrecta. ({intentos}/3)')
      else:
         validacion = True
   if validacion == False:
      print('Haz alcanzado el limite de intentos, se cerrara el programa.')
   return validacion

def en_construccion():
   print("En construcción...")

def mostrar_menu_principal():
   print('---------- MENU PRINCIPAL ----------')
   print("1 - Gestión de Aerolíneas.")
   print("2 - Aprobar/Denegar Promociones")
   print("3 - Gestión de Novedades")
   print("4 - Reportes")
   print("0 - Salir\n")

def Submenu1():
      print("\n........Gestion de Aerolineas.........")
      print("1- Crear Aerolinea")
      print("2- Modificar Aerolinea")
      print("3- Eliminar Aerolinea")
      print("4- Volver")
      MENU2()


def Submenu2():
      print("\n........Aprobar/Denegar Promociones.........")
      en_construccion()


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
         case 1: en_construccion()
         case 2: en_construccion()
         case 3: en_construccion()
         case 4: print(" \nVolviendo al menú principal...")

def menuAdmin():
   opc = 1
   while (opc != 0):
      mostrar_menu_principal()
      opc = int(input("Ingrese su opción: "))
      match opc:
         case 1: Submenu1()  
         case 2: Submenu2()  
         case 3: Submenu3()  
         case 4: Submenu4()  
         case 0: pass
         case _: print('Opción inválida!')

## INÍCIO
def main():
   system('cls')
   if login() == True:
      menuAdmin()
      print('Gracias por usar nuestro sistema.')
main()