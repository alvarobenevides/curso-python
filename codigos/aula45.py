"""
Iterável -> str, range, ect (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue sue interador
"""
texto = 'Álvaro'  # iterável
# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break
for letra in texto:
    print(letra)
