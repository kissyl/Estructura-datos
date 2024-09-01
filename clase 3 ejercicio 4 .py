import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

longitud_contrasena = 12
nueva_contrasena = generar_contrasena(longitud_contrasena)
print(f"Contraseña generada de {longitud_contrasena} caracteres: {nueva_contrasena}")

for longitud in [8, 16, 20]:
    print(f"Contraseña de {longitud} caracteres: {generar_contrasena(longitud)}")