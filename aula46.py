"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto

texto = iter('Felix')  # iterável
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador) # iterador
        print(letra)
    except StopIteration:
        break    