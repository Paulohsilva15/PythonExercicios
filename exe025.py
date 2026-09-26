nome = str(input('Qual o seu nome?'))
idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('{} você é maior de idade ! '.format(nome))
else:
    print('{} você é menor de idade !'.format(nome))