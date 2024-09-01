#solicitar los numeros y la operacion 
  num1 = int(input("Introduce el primer numero: "))
  num2 = int(input("Introduce el segundo numero: "))
  operacion = input("Introduce la operacion (+, -, *, /): ")

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