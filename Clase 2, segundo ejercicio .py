# Pares
pares = [i for i in range (2,101,2) ]
print (pares)


# Triangulo astericos 
altura = 5 
for i in range (1, altura + 1):
    print ("*" * i)


# Promedio
import random
numeros = [random.randint(1, 100)for _ in range (10)]
promedio = sum(numeros)/ len(numeros)
print ("numeros:", numeros ) 
print ("promedio:", promedio)


def factorial (n):
    if n == 0 or n == 1: 
        return 1 
    else: 
        return n * factorial(n - 1) 
 
numero = 5
resultado = factorial( numero)
print (f" el resultado de {numero} es {resultado}")

 

