# Aula 8 - Laços de Repetição ("For")

"""
# 0, 1, 2, 3, 4
for var in range(5):
    print(var)
"""

"""
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for var in range(0, 10):
    print(var)
"""

"""
# 0, 2, 4, 6, 8
for var in range(0, 10, 2):
    print(var)
"""

soma = 0
for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota

print(f'A média de suas notas é: {(soma / 3):.2f}')

