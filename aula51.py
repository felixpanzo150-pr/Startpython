"""
Listas  em Python
Tipos list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métods úteis: 
  append - Adiciona um item ao final.
  insert - Adiciona um item no indice escolhido.
  pop - Remove do final ou do indice.
  del - apaga um indice 
  clear - limpa a lista
  extend - estende a lista.
  + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_a)
print(lista_a)