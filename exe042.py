primeiro = int(input('Primeiro Segmento: '))
segundo = int(input('Segundo Segmento: '))
terceiro = int(input('Terceiro Segmento: '))

if primeiro + segundo > terceiro and primeiro + terceiro > segundo and segundo + terceiro > primeiro:
    if primeiro == segundo and primeiro == terceiro:
        print('Os segmentos acima podem formar um Triângulo Equilátero')
    elif primeiro != segundo and segundo != terceiro and primeiro != terceiro:
        print('Os segmentos acima podem formar um Triângulo Escaleno')
    else:
        print('Os segmentos acima podem formar um Triângulo Isósceles')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')