from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Escolha uma opção
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 10)
print('-=' * 10)

if jogador < 0 or jogador > 2:
    print('Jogada Inválida')

else:
    print('computador jogou {}'.format(itens[computador]))
    print('jogador jogou {}'.format(itens[jogador]))

    print('-=' * 10)

    if computador == 0:  # computador jogou Pedra
        if jogador == 0:
            print('EMPATE')

        elif jogador == 1:
            print('JOGADOR VENCE')

        elif jogador == 2:
            print('COMPUTADOR VENCE')

    elif computador == 1:  # computador jogou Papel
        if jogador == 0:
            print('COMPUTADOR VENCE')

        elif jogador == 1:
            print('EMPATE')

        elif jogador == 2:
            print('JOGADOR VENCE')

    elif computador == 2:  # computador jogou Tesoura
        if jogador == 0:
            print('JOGADOR VENCE')

        elif jogador == 1:
            print('COMPUTADOR VENCE')

        elif jogador == 2:
            print('EMPATE')

