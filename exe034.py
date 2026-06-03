salario = float(input('qual é o valor do salario do funcionario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava r$ {:.2f} passa a ganhar {:.2f} agora.'.format(salario,novo))