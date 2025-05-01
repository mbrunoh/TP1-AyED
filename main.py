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
      user, contrasena: string
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

cant_ARG = 0
cant_CHI = 0
cant_BRA = 0

def login():
   validacion = False
   intentos = 0
   while intentos < 3 and validacion == False:
      user = input('Ingrese nombre de Usuario: ').lower()
      contrasena = maskpass.advpass('Ingrese la Contraseña: ')
      if user != ADMIN_USER or contrasena != ADMIN_CONTRASENA:
         intentos += 1
         print(f'Nombre de Usuario o Contraseña incorrecta ({intentos}/3).')
         sleep(1)
         system('cls')
      else:
         validacion = True
   if validacion == False:
      print('Haz alcanzado el limite de intentos, se cerrara el programa.')
   return validacion

def menu_administrador():
   opc = 0
   while (opc != 5):
      system('cls')
      print('---------- Menú del Administrador ----------')
      print('1 - Gestión de Aerolíneas')
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
      opc = input('Ingrese su opción: ').lower()
      match opc:
         case 'a': submenu_1a()
         case 'b': en_construccion() 
         case 'c': en_construccion() 
         case 'd': pass
         case _:
            print('Opción inválida!')
            sleep(1)

def submenu_1a():
   system('cls')
   print('---------- Gestión de Aerolíneas ----------')
   print('a - Crear Aerolínea\n')
   global cant_ARG, cant_BRA, cant_CHI
   
   new_aerolinea = True
   while new_aerolinea:
      nombre_aerolinea = input('Nombre de la Aerolínea: ')
      val_codigoIATA = False
      while not val_codigoIATA:
         codigoIATA = input('Informe el código IATA (máximo 3 caracteres): ')
         if len(codigoIATA) <= 3 and len(codigoIATA) > 0:
            val_codigoIATA = True
         else:
            print('¡Código IATA inválido!')
      val_codigoPAIS = False
      while not val_codigoPAIS:
         print('Informe el código del país.')
         print('ARG - Argentina')
         print('BRA - Brasil')
         print('CHI - Chile')
         codigoPAIS = input('\nCódigo: ').upper()
         if codigoPAIS == 'ARG' or codigoPAIS == 'CHI' or codigoPAIS == 'BRA':
            val_codigoPAIS = True
         else:
            print('¡Código del país inválido!')
      match codigoPAIS:
         case 'ARG': cant_ARG += 1
         case 'CHI': cant_CHI += 1
         case 'BRA': cant_BRA += 1

      val_opc = False
      while not val_opc:
         opc = input(f'¡Aerolínea {nombre_aerolinea} cadastrada con suceso! Desea cadastra una nueva aerolínea? (s/n) ').lower()
         match opc:
            case 'no' | 'n':
               val_opc = True
               new_aerolinea = False
            case 'si' | 's':
               pass
               val_opc = True
            case _:
               print('Opción inválida!')
   mostrar_cantidades()

def mostrar_cantidades():
   system('cls')
   # Cantidades diferentes
   if cant_BRA > cant_CHI and cant_CHI > cant_ARG:
      print(f'Brasil tiene la mayor cantidad de aerolínea, {cant_BRA}.')
      print(f'Argentina tiene la menor cantidad de aerolínea, {cant_ARG}.')
   elif cant_BRA > cant_ARG and cant_ARG > cant_CHI:
      print(f'Brasil tiene la mayor cantidad de aerolínea, {cant_BRA}.')
      print(f'Chile tiene la menor cantidad de aerolínea, {cant_CHI}.')
   elif cant_ARG > cant_CHI and cant_CHI > cant_BRA:
      print(f'Argentina tiene la mayor cantidad de aerolínea, {cant_ARG}.')
      print(f'Brasil tiene la menor cantidad de aerolínea, {cant_BRA}.')
   elif cant_ARG > cant_BRA and cant_BRA > cant_CHI:
      print(f'Argentina tiene la mayor cantidad de aerolínea, {cant_ARG}.')
      print(f'Chile tiene la menor cantidad de aerolínea, {cant_CHI}.')
   elif cant_CHI > cant_ARG and cant_ARG > cant_BRA:
      print(f'Chile tiene la mayor cantidad de aerolínea, {cant_CHI}.')
      print(f'Brasil tiene la menor cantidad de aerolínea, {cant_BRA}.')
   elif cant_CHI > cant_BRA and cant_BRA > cant_ARG:
      print(f'Chile tiene la mayor cantidad de aerolínea, {cant_CHI}.')
      print(f'Argentina tiene la menor cantidad de aerolínea, {cant_ARG}.')
   # 2 con la misma cantidad
   elif cant_BRA == cant_ARG and cant_ARG > cant_CHI:
      print(f'Brasil y Argentina tienen la mayor cantidad de aerolínea, {cant_BRA} cada.')
      print(f'Chile tiene la menor cantidad de aerolínea, {cant_CHI}.')
   elif cant_BRA == cant_CHI and cant_CHI > cant_ARG:
      print(f'Brasil y Chile tienen la mayor cantidad de aerolínea, {cant_BRA} cada.')
      print(f'Argentina tiene la menor cantidad de aerolínea, {cant_ARG}.')
   elif cant_ARG == cant_CHI and cant_CHI > cant_BRA:
      print(f'Argentina y Chile tienen la mayor cantidad de aerolínea, {cant_ARG} cada.')
      print(f'Brasil tiene la menor cantidad de aerolínea, {cant_BRA}.')
   elif cant_BRA == cant_ARG and cant_ARG < cant_CHI:
      print(f'Chile tiene la mayor cantidad de aerolínea, {cant_CHI}.')
      print(f'Brasil y Argentina tienen la menor cantidad de aerolínea, {cant_BRA} cada.')
   elif cant_BRA == cant_CHI and cant_CHI < cant_ARG:
      print(f'Argentina tiene la mayor de cantidad de aerolínea, {cant_ARG}.')
      print(f'Brasil y Chile tienen la menor cantidad de aerolínea, {cant_BRA} cada.')
   elif cant_ARG == cant_CHI and cant_CHI < cant_BRA:
      print(f'Brasil tiene la mayor cantidad de aerolínea, {cant_BRA}.')
      print(f'Argentina y Chile tienen la menor cantidad de aerolínea, {cant_ARG} cada.')
   # Todos con la misma cantidad
   else:
      print(f'Argentina, Brasil y Chile tienen la misma cantidad de aerolínea, {cant_ARG} cada.')
   pass_var = input('\nPresione una tecla para continuar... ')

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
main()