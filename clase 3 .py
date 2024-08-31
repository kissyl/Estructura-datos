def calculofactorial (numero:int )->int:
    resultado: int
    if numero < 0 :
        return "No se puede valores negativos"
    elif numero == 0:
        return 1
    
    for n in range (1,numero +1):
        resultado = resultado * n
        
