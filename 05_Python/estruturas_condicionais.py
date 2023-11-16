# Aula 6 - Estruturas Condicionais

idade = 16
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Vocé menor de idade')


"""
    Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média
    superior ou igual à 7, e "Reprovado(a)", caso a média seja inferior a 7.
"""
nota_media = float(input('Qual a sua nota média? '))
if nota_media >= 7:
    print('Você está Aprovado(a)')
elif nota_media >= 5:
    print('Você está de Recuperação')
else:
    print('Você está Reprovado(a)')

media_final = 8
presenca = 80
if media_final >= 7 and presenca >= 70:
    print('Você está Aprovado(a)')
    print('Parabéns')
else:
    print('Você está Reprovado(a)')
    print('Tente Novamente')