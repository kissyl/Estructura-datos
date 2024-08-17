# solicita 3 numeros 
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3593304934.
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))
# Suggested code may be subject to a license. Learn more: ~LicenseLog:935061142.
# Determinar el mayor 
mayor = num1
if num2 > mayor:
  mayor = num2
if num3 > mayor:
  mayor = num3
print("El mayor es", mayor)
# Determinar el menor 
menor = num1
if num2 < menor:
  menor = num2
if num3 < menor:
  menor = num3
print("El menor es", menor)
#solicitar numero 
num = int(input("Introduce un numero: "))
# Determinar si es par o impar 
if num % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")

  # los numeros y la operacion 
  num1 = int(input("Introduce el primer numero: "))
  num2 = int(input("Introduce el segundo numero: "))
  operacion = input("Introduce la operacion (+, -, *, /): ")
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2025336748.
  # Realizar la operacion y mostar el resultado 
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2027596818.
  if operacion == "+":
    resultado = num1 + num2
  elif operacion == "-":
    resultado = num1 - num2
  elif operacion == "*":
    resultado = num1 * num2
  elif operacion == "/":
    resultado = num1 / num2
  else:
    print("Operacion no valida")
  print("El resultado es", resultado)

  #solicitar peso y altura 
  peso = float(input("Introduce tu peso en kg: "))
  altura = float(input("Introduce tu altura en metros: "))
  # Calcular el IMC 
  imc = peso / altura ** 2
  # Mostrar el resultado 
  print("Tu IMC es", imc) 
  # determinar si tiene sobre peso y mostrar el resultado
  if imc < 18.5:
    print("Tienes bajo peso")
  elif imc >= 18.5 and imc < 25:
    print("Tienes un peso normal")
  if imc > 25:
    print("Tienes sobrepeso")
  else:
    print("No tienes sobrepeso")
