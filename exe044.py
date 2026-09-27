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
    print('Sua compra de R${:.2f} vai custar R${:.2f} com o desconto de 10%'.format(compra,valor))
elif opção == 2:
    valor = compra - (compra * 5 / 100)
    print('Sua compra de R${:.2f} no cartão vai custar {:.2f} com desconto de 5%'.format(compra,valor))
elif opção == 3:
    valor = compra / 2
    print('Sua compra de R${:.2f} em 2x fica {:.2f}'.format(compra,valor))
elif opção == 4:
    valor = compra + (compra * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    total = valor / parcela

    print(' Sua compra de R${:.2f} ficará {:.2f} com juros de 20% '.format(compra,valor))
    print('A quantidade de parcelas em {}x fica {:.2f}'.format(parcela,total))




