"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta qualquer
e vai dar a possibilidade para o usuário digitar
apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir
 se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma ltra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'

    print('Palavra_formatada:', palavra_formatada)

    if palavra_formatada == palavra_secreta:
        os.system('cls') 
        print('VOCÊ GANHOU!! PARABENS!') 
        print('A palavra era', palavra_secreta) 
        print('Tentativas:', numero_tentativas)
         

  