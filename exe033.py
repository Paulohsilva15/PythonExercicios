a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# verificando o menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

# verificando o maior
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))