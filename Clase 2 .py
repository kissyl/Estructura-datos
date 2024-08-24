# sistema control ingreso }
cupo_maximo= 50 
cupo_actual= 0

while cupo_actual < cupo_maximo:

   valido= input("boleto valido")
   if valido == "5,6,7,8,9,10" :
      print("ingresa")
      control = control +5

   else :
      print("no ingresa")
      
print("cupo completo")

