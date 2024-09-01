from sympy import resultant


operacion = input ("operacion (suma,resta ,multiplicacion, division): ")
num1 = int(input("primer numero"))
num2 = int(input("segundo numero"))

if operacion =='suma': 
    resultado= num1 + num2 
elif operacion == 'resta':
    resultado= num1 - num2
elif operacion== 'multiplicacion':
    resultado= num1 * num2
elif operacion == 'division':
    resultado= num1 / num2
else:
    print ("operacion no valida ")
print(" el resultado es", resultado )






    