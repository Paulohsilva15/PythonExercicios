preço = float(input('Qual o valor do produto? R$'))
novo = preço - preço * 5 / 100
print ('O produto que custava R$ {:.2f}, na promoção com desconto de 5% fica R$ {:.2f}'.format(preço,novo))