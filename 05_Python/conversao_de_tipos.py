# Aula 5 - Conversão de Tipos

idade = '26'
num1 = '10'
num2 = '20'

print(num1 + num2)

print(idade, type(idade))
idade_inteira = int(idade)

"""
Funções de conversão:
    - str(): converter para string
    - int(): converter para inteiro
    - float(): converter para float
    - bool(): converter para booleano
"""

# Convertendo os tipos
altura = input('Qual é a sua altura? ')

print(altura, type(altura))

altura_real = float(input('Qual é a sua altura em metros? '))
print(altura_real, type(altura_real))