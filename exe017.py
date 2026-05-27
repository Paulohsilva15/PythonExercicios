#faça um programa que leia o comprimento do cateto
#oposto e do cateto adjacente de um triângulo, calcule
#e mostre o comprimento da hipotenusa.

#co = float(input('digite o cateto oposto:'))
#ca = float(input('digite o cateto adjacente:'))
#hi = (co ** 2 + ca ** 2) ** (1/2)

#print('A hipotenusa vai medir {:.2f}'.format(hi))

#import math
#co = float(input('digite o cateto oposto:'))
#ca = float(input('digite o cateto adjacente:'))
#hipotenusa = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

from math import hypot
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hipotenusa = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))