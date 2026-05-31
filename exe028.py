from random import choice

print('diga um numero inteiro de 0 a 5')
jogador = (int(input('qual número de o a 5 ? ')))

lista = [0,1,2,3,4,5]

escolhido = choice(lista)

if jogador == escolhido:
    print('Parabéns você acertou ! {}'.format(escolhido))
else:
    print ('Tente novamente! o número era {} '.format(escolhido))