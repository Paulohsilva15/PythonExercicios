nota1 = float(input('Digite a primeira nota :' ))
nota2 = float(input('Digite a segunda nota :'))

media = (nota1 + nota2)/2

if media >=6:
    print('Sua media foi maior que 6, \033[32m Aprovado \033[m !')
else:
    print('Sua media foi menor que 6,\033[31m Estude Mais \033[m ')

print('A média do aluno foi {}' .format(media))
