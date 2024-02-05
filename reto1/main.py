# Programa donde se va a solicitar los datos de:
# - Nombre(s)
# - Apellidos
# - Número de teléfono
# - Correo electrónico.

#Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

#Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico .
import re


validaciontelefono = False
validacioncorreoelectronico = False
expresionregular_correoElectronico = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

nombres = input("Ingresa por favor tu(s) nombre(s):\n ")
apellidos = input("Ingresa por favor tu(s) apellidos:\n ")
while validaciontelefono==False:
  nrotelefonico = input("Ingresa por favor tu número de teléfono (Ej. 4621236547):\n ")
  try:
    nrotelefonico = int(nrotelefonico)
    if nrotelefonico != "" :
      validaciontelefono = True
  except ValueError:
    print ("La entrada es incorrecta: escribe un numero entero")
while validacioncorreoelectronico==False:
  correoelectronico = input("Ingresa por favor tu correo electrónico (Ej. otro@otro.com):\n ")
  if re.match(expresionregular_correoElectronico, correoelectronico):
    validacioncorreoelectronico = True

## Imprimir la expresión correspondiente.
print(f'Hola {nombres} {apellidos}, el número de teléfono registrado es "{nrotelefonico}" y en breve recibiras un correo electrónico de bienvenida a "{correoelectronico}".')