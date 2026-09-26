nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Nota {} e {} fica com Media {:.1f}!'.format(nota1, nota2, media))
    print('Aluno Reprovado')
elif media >= 5 and media <= 6.9:
    print('Nota {} e {} fica com Media {:.1f}!'.format(nota1, nota2, media))
    print('Aluno em Recuperação')
else:
    print('Nota {} e {} fica com Media {:.1f}!'.format(nota1, nota2, media))
    print('Aluno Aprovado')




