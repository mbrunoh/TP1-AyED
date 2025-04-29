import maskpass
##VARIABLES USUARIOS##
#int: codUsuario
#string: nombreUsuario(100), claveUsuario(8), tipoUsuario(20), emailUsuario(100), telefonoUsuario(20)
######################

##VARIABLES AEROLINEAS#
#int: codAerolionea
#string: nombreAerolinea(100), codigoIATA(3), descripcionAerolinea(200), codPais(3) 
######################

##VARIABLES NOVEDADES##
#int: codNovedad
#string: textoNovedad(200), fechaPublicacionNovedad(10), fechExpiracionNovedad(10)  
######################

##VARIABLES EXTRA##
#int: i, opc, opc2
#string: nombreUsuario, claveUsuario, contra, usr
######################

###Declaraicon de Variables
nombreUsuario = "admin@ventaspasajes777.com"
claveUsuario = "admin"
loginok = True
###


def login():
   i = 0
   global loginok
   while loginok : 
      usr = input("Ingrese nombre de Usuario: ")
      contra = maskpass.advpass("Ingrese la Clave: ")
      if usr != nombreUsuario or contra != claveUsuario:
         print("Nombre de Usuario o contraseña inexistente.")
         i = i+1
         if i == 3: 
            print("Haz alcanzado el limtie de intentos, se cerrara el programa.")
            loginok = False
      else:
         menuAdmin()
   
 

def cartel():
   print("\n....en construcción...")

def MENU():
   print("\n........MENU PRINCIPAL.........")
   print("1- Gestion de Aerolineas.")
   print("2- Aprobar/Denegar Promiciones")
   print("3- Gestion de Novedades")
   print("4- Reportes")
   print("0- Salir")


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
   global loginok
   opc = 1
   while (opc != 0):
      MENU()
      opc = int(input("Ingrese su opcion: "))
      while (opc < 0 or opc > 4):
         opc = int(input("Ingrese una opcion Valida: "))
      
      match opc:
         case 1: Submenu1()  
         case 2: Submenu2()  
         case 3: Submenu3()  
         case 4: Submenu4()  
         case 0: 
            print("\nGracias por usar nuestro sistema")
            loginok = False

##inicio
login()













