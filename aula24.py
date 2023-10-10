# Operador in e not in
# String são iteráveis(Navegação por parte)
# 0 1 2 3 4 
# f e l i x
# -5-4-3-2-1
nome ='Félix'
# print(nome[-4])
# print(nome[2])
#print('lix' in nome)
#print('p' in nome)
#print(10 * '-')
#print('Fel' not in nome)
#print('zero' in nome)
 # condição(Se l estiver na váriavel nome, então retorna True or False)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque você deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
print('Mais alguma coisa ?')    



