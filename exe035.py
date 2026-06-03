r1 = float(input('Primeiro segmanto: '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))

if r1 < r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('os segmentos acima podem formar um triangulo !')
else:
    print ('o segmento não pode formar um triangulo !')
