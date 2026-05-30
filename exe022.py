nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Quantas letras tem o seu nome {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {}'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
