n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

op = input('Digite + para somar ou * para multiplicar: ')

if op == '+':

    print('o resultado de {:.0f} e {:.0f} será {:.0f}'.format(n1, n2, n1+n2))
else:

    print('o resultado de {:.0f} e {:.0f} será {:.0f}'.format(n1, n2, n1*n2))