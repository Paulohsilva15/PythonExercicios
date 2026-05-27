# um professor quer sortear um dos seus alunos para apagar o quadro
#faça um programa que ajude a sortear o nome de um deles

from random import choice
n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
