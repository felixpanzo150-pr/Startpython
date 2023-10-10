"""
Listas  em Python
Tipos list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métods úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[2]
#print(lista)
#print(lista[2])
#lista.append(50)
#lista.pop()
#lista.append(60)
lista.append('Paulo')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(100, 5)
print(lista[4])