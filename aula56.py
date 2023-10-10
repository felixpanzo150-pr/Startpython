"""
Faça um progroma de compra com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros de indices enexistentes na lista.
"""
import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')


        # Tratamento de erro com except:
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('por favor digite o número int.')
        except IndexError:
            print('índice não existe na lista')
        except Exception:
            print('Erro desconhecido')          
        #print('a')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)     
    else:
        print('Por favor, escolha i, a ou l.')
     