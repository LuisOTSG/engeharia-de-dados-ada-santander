# Aula 11 - Funções

# 1. O que são funções?
"""
Exemplos de funções
    - print(): Imprime uma mensagem (int, float, str) no console (terminal, cmd, notebook)
    - input(): Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
    - len(): Recebe uma lista e retorna o tamanho dessa lista
    - max(): Retorna o maior valor de uma lista
"""

# 2. Criação de funções

# Função inicial
def saudacao():
    print('Seja bem-vindo(a)')
    print('É um prazer estar realizando essa trilha de Engenharia de Dados.')

saudacao()
saudacao()
saudacao()

# Funções com parâmetros
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}')
    print(f'É um prazer estar realizando essa trilha de {curso}.')

saudacao('Luis', 'Engenharia de Dados')
saudacao('Flavia', 'Ciência de Dados')

# Funções com parâmetros default
def saudacao(nome, curso='Engenharia de Dados'):
    print(f'Seja bem-vindo(a), {nome}')
    print(f'É um prazer estar realizando essa trilha de {curso}.')

saudacao('Luis')

# Funções com return
def soma(num1, num2):
    return num1 + num2
    # Nada abaixo de return funciona mais

resultado = soma(5, 7)
print('A soma é igual a', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    else:
        return num1 / num2

resultado_soma = calculadora(10, 20)
print(resultado_soma)

resultado_multiplicacao = calculadora(10, 20, '*')
print(resultado_multiplicacao)