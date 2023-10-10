"""
Fatiamento de strings
012345678
olá mundo
-987654321
Fatiamento [i - início:f - fim:p - passo(quantos caracteres ele vai pular)] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-4])
print(variavel[4:])
print(variavel[:4])
print(variavel[-8:-2])
print(len(variavel[3]))
print(variavel[0:len(variavel):1])
print(variavel[::-1])




