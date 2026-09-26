peso =float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Cuidado está Abaixo do Peso')
elif imc <= 25:
        print('O IMC dessa pessoa é de {:.1f}'.format(imc))
        print('Parabéns , está no peso normal')
elif imc <= 30:
        print('O IMC dessa pessoa é de {:.1f}'.format(imc))
        print('Você está no sobrepeso')
elif imc <= 40:
        print('O IMC dessa pessoa é de {:.1f}'.format(imc))
        print('Você está no Obesidade')
else:
        print('O IMC dessa pessoa é de {:.1f}'.format(imc))
        print(' Obesidade Mórbida')