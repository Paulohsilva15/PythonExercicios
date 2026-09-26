idade = int(input('Qual a sua idade?'))
if idade <= 9:
    print('Você é criança!')
elif idade >= 10 and idade <= 14:
    print('Você é pré-adolescente!')
elif idade  >= 15 and idade <= 17:
    print('Você é adolescente!')
elif idade >= 18 and idade <= 30:
    print('Você é adulto')
elif idade >=31 and idade <= 60:
    print('Está na melhor idade')
else:
    print('Você é idoso')