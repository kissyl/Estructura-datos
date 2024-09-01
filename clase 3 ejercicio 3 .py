def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    
    return palabra == palabra[::-1]

palabras_prueba = ["oso", "radar", "luna", "a luna ese anula", "somos"]

for palabra in palabras_prueba:
    if es_palindromo(palabra):
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')