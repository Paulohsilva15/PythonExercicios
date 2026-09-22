nome = str(input('Qual o seu nome? '))
print('''Escolha uma das Opções:
[1] Você é o Paulo?
[2] Você não é a Paulo?
[3] Talvez seja o Paulo?''')

opção = int(input('Sua opção: '))
if opção == 1:
        print ('Podemos ir ao cinema?')
elif opção == 2:
        print('Você é Curioso (a)')
elif opção ==3:
        print('Você pode provar??')
else:
    print('Essa opção não é aceita!')

