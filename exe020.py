from random import choice, shuffle

n1 = str(input('digite o primeiro nome: '))
n2 = str(input('digite o segundo nome: '))
n3 = str(input('digite o terceiro nome: '))
n4 = str(input('digite o quarto nome: '))
lista = [n1, n2, n3, n4]

shuffle(lista)

print('A ordem de apresentação será {}')
print(lista)

