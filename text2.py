velocidade = int(input('Digite o valor da velocidade : '))

if velocidade > 80:
    print('Você Foi Multado !!')
    multa = (velocidade - 80)*7
    print('o valor da multa é {:.2f}'.format(multa))
    if velocidade > 120:
        print('Infração  Gravissima')
else:
    print('Está no Permitido, Boa Viagem!')
