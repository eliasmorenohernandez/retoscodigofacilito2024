# Programa donde se va a solicitar los datos de:
# - Nombre(s)
# - Apellidos
# - Número de teléfono
# - Correo electrónico.

#Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

#Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico .
import re



expresionregular_correoElectronico = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
validacionnumusuariosregistrar=False
while validacionnumusuariosregistrar==False:
  #Se obtiene el número de usuarios posibles a registrar
  numusuariosaregistrar = input("Ingresa el número de usuarios que deseas registrar mayor a 0:\n ")
  try:
    numusuariosaregistrar = int(numusuariosaregistrar)
    if numusuariosaregistrar != "" and numusuariosaregistrar > 0:
      validacionnumusuariosregistrar = True
  except ValueError:
    print ("La entrada es incorrecta: escribe un numero entero mayor a 0")
#Contabilizar el número de usuarios registrados.    
numusuariosregistrados = 1
nrocaracteresminimos = 5
nrocaracteresmaximos = 50
nrocaracterestelefono = 10
while numusuariosregistrados <= numusuariosaregistrar :
  print(f"Datos a capturar de usuario número '{numusuariosregistrados}':\n") 
  validaciontelefono = False
  validacioncorreoelectronico = False   
  validacionnombre = False
  validacionapellidos = False
  while validacionnombre == False:
    nombres = input(f"Ingresa por favor tu(s) nombre(s) con un mínimo de {nrocaracteresminimos} caracteres y un máximo de {nrocaracteresmaximos} caracteres:\n ")
    if len(nombres)>=nrocaracteresminimos and len(nombres)<=nrocaracteresmaximos:
      validacionnombre = True
  while validacionapellidos == False:
    apellidos = input(f"Ingresa por favor tu(s) apellidos con un mínimo de {nrocaracteresminimos} caracteres y un máximo de {nrocaracteresmaximos} caracteres:\n ")
    if len(apellidos)>=nrocaracteresminimos and len(apellidos)<=nrocaracteresmaximos:
      validacionapellidos = True
  while validaciontelefono==False:
    nrotelefonico = input(f"Ingresa por favor tu número de teléfono con '{nrocaracterestelefono}' caracteres (Ej. 4621236547):\n ")
    try:
      nrotelefonico = int(nrotelefonico)
      if nrotelefonico != "" and len(str(nrotelefonico))==nrocaracterestelefono:
        validaciontelefono = True
    except ValueError:
      print (f"La entrada es incorrecta: escribe un numero de teléfono con '{nrocaracterestelefono}' caracteres")
  while validacioncorreoelectronico==False:
    correoelectronico = input(f"Ingresa por favor un correo electrónico valido con un mínimo de {nrocaracteresminimos} caracteres y un máximo de {nrocaracteresmaximos} caracteres (Ej. otro@otro.com):\n ")
    if re.match(expresionregular_correoElectronico, correoelectronico) and len(correoelectronico)>=nrocaracteresminimos and len(correoelectronico)<=nrocaracteresmaximos:
      validacioncorreoelectronico = True
  ## Imprimir la expresión correspondiente.
  print(f"Registro de usuario número '{numusuariosregistrados}':\n")    
  print(f'Hola {nombres} {apellidos}, el número de teléfono registrado es "{nrotelefonico}" y en breve recibiras un correo electrónico de bienvenida a "{correoelectronico}".')
  numusuariosregistrados += 1
