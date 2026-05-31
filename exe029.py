velo = float(input('Qual a velocidade do carro: '))
if velo > 80:
    print('Você foi multado')
    multa = (velo - 80) * 7
    print('o valor da multa por  7 reais o km é de {:.2f}'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')
