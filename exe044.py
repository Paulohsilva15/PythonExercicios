print ('========== Lojas do Vila Rica ==========')
compra = float(input('Preço do produto? R$'))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Digite uma das opção'))

if opção == 1:
    valor = compra - (compra * 10 / 100)
    print('O Valor escolhido fica {:.2f} com o desconto de 10%'.format(valor))
elif opção == 2:
    valor = compra - (compra * 5 / 100)
    print('O Valor escolhido no cartão {:.2f} com desconto de 5%'.format(valor))
elif opção == 3:
    valor = compra / 2
    print('O Valor escolhido parcelado em 2x fica {:.2f}'.format(valor))
elif opção == 4:
    valor = compra + (compra * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    total = valor / parcela

    print(' O valor à mais no cartão com 20% de juros fica {:.2f} '.format(valor))
    print('A quantidade de parcelas em {}x fica {:.2f}'.format(parcela,total))




