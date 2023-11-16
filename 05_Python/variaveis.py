# Aula 3 - Variáveis

# Criando uma variável
idade = 25

# Imprimindo uma variável
print(idade)

# Criando e imprimindo mais variáveis
nome = 'Luis Gomes'
print(nome)

"""
Tipos de variáveis:
    1. int - números inteiros, ou seja, números sem a parte decimal: 5, 25, 64, -3, 1000
    2. float - números reais, ou seja, números com a parte decimal: 5.0, 25.4, 3.14, -32
    3. str - cadeias de caracteres, ou seja, dados textuais
    4. bool - valores lógicos (booleanos): True ou False
"""

# Verificando o tipo das variáveis
idade = 25
altura = 1.72
nome = 'Luis Otávio'
estudando = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))

# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual a linguagem de programação você está estudando? ')
print('A linguagem que você está estudando é', linguagem)
print(type(linguagem))