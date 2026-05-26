largura = float(input('qual a largura da parede? '))
altura = float(input('qual a altura da parede? '))
area = largura * altura
print ('Sua parede tem a dimensâo de {} x {} e sua area é de {}m2'.format(largura,altura,area))
tinta = area / 2
print ('Para pintar essa parede, você precisará {}l de tinta'.format(tinta))