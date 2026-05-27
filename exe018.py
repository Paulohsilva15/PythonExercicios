# faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno ,cosseno e tangente desse ângulo.

import math
#ângulo = float(input('digite o ângulo que deseja: '))
#seno = math.sin(math.radians(ângulo))
#print ('O ângulo de {} tem o seno de {:.2f} '.format(ângulo, seno))

#cose =  math.cos(math.radians(ângulo))
#print('O ângulo de {} tem o cosseno de {:.2f} '.format(ângulo, cose))

#tan = math.tan(math.radians(ângulo))
#print ('O ângulo de {} tem o  tangente de {:.2f} '.format(ângulo, tan))

#maneira simplificada
from math import radians, sin, cos, tan
ângulo = float(input('digite o ângulo que deseja: '))
seno = sin(math.radians(ângulo))
print ('O ângulo de {} tem o seno de {:.2f} '.format(ângulo, seno))

cose =  cos(math.radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f} '.format(ângulo, cose))

tan = tan(math.radians(ângulo))
print ('O ângulo de {} tem o  tangente de {:.2f} '.format(ângulo, tan))