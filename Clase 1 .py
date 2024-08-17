#solicitar 3 numeros 
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
