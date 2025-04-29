import maskpass
from time import sleep
from os import system

"""
# Variables Globales
   ADMIN_USER: string (CONSTANTE)
   ADMIN_CONTRASENA: string (CONSTANTE)

# Variables Locales (Por función)
   login()
      validacion: bolean
      intentos: int
      user, contrasena: char
   menu_administrador()
      opc: int
   submenu_1()
      opc: string
   submenu_3()
      opc: string
   submenu_4()
      opc: string
"""

ADMIN_USER = 'admin' # admin@ventaspasajes777.com
ADMIN_CONTRASENA = 'admin'

def login():
   validacion = False
   intentos = 0
   while intentos < 3 and validacion == False:
      user = input('Ingrese nombre de Usuario: ')
      contrasena = maskpass.advpass('Ingrese la Contraseña: ')
      if user != ADMIN_USER or contrasena != ADMIN_CONTRASENA:
         intentos += 1
         print(f'Nombre de Usuario o Contraseña incorrecta ({intentos}/3).')
         sleep(1)
         system('cls')
      else:
         validacion = True
   return validacion

def menu_administrador():
   opc = 0
   while (opc != 5):
      system('cls')
      print('---------- Menú del Administrador ----------')
      print('1 - Gestión de Aerolíneas.')
      print('2 - Aprobar/Denegar Promociones')
      print('3 - Gestión de Novedades')
      print('4 - Reportes')
      print('5 - Salir\n')
      try: # Como las opciones serán comparadas con números enteros (int), hacemos una validacion previa del dato ingresado.
         opc = int(input('Ingrese su opción: '))
      except: # Si no es posible converter el dato en numero, es porque el usuario ingresó una opción inválida.
         print('Opción inválida!')
         sleep(1)
      else:
         match opc:
            case 1: submenu_1()  
            case 2: submenu_2()
            case 3: submenu_3()  
            case 4: submenu_4()  
            case 5: pass
            case _:
               print('Opción inválida!')
               sleep(1)

def en_construccion():
   print('En construcción...')
   sleep(1)

def submenu_1(): # Gestión de Aerolíneas
   opc = ''
   while (opc != 'd'):
      system('cls')
      print('---------- Gestión de Aerolíneas ----------')
      print('a - Crear Aerolínea')
      print('b - Modificar Aerolínea')
      print('c - Eliminar Aerolínea')
      print('d - Volver\n')
      opc = input('Ingrese su opción: ')
      match opc:
         case 'a': en_construccion()
         case 'b': en_construccion() 
         case 'c': en_construccion() 
         case 'd': pass
         case _:
            print('Opción inválida!')
            sleep(1)

def submenu_2(): # Aprobar/Denegar Promociones
   en_construccion()

def submenu_3(): # Gestión de Novedades
   opc = ''
   while (opc != 'e'):
      system('cls')
      print('---------- Gestión de Novedades ----------')
      print('a - Crear Novedad')
      print('b - Modificar Novedad')
      print('c - Eliminar Novedad')
      print('d - Ver Novedades')
      print('e - Volver\n')
      opc = input('Ingrese su opción: ')
      match opc:
         case 'a': en_construccion()
         case 'b': en_construccion() 
         case 'c': en_construccion()
         case 'd': en_construccion() 
         case 'e': pass
         case _:
            print('Opción inválida!')
            sleep(1)

def submenu_4(): # Reportes
   opc = ''
   while (opc != 'd'):
      system('cls')
      print('---------- Reportes ----------')
      print('a - Reporte de Ventas (reservas con estado “confirmada”)')
      print('b - Reporte de Vuelos')
      print('c - Reporte de Usuarios')
      print('d - Volver\n')
      opc = input('Ingrese su opción: ')
      match opc:
         case 'a': en_construccion()
         case 'b': en_construccion() 
         case 'c': en_construccion()
         case 'd': pass
         case _:
            print('Opción inválida!')
            sleep(1)

# Início
def main():
   system('cls')
   if login() == True:
      system('cls')
      menu_administrador()
      print('Gracias por usar nuestro sistema.')
   else:
      print('Haz alcanzado el limite de intentos, se cerrara el programa.')
main()