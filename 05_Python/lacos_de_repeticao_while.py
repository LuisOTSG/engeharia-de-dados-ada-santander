# Aula 7 - Laços de Repetição ("While")

num_sorteio = 3
num_usuario = float(input('Escolha um número de 1 a 10: '))

while num_usuario != num_sorteio:
    print('Você errou. Tente Novamente')
    num_usuario = float(input('Escolha um número de 1 a 10: '))

print('Parabés, você acertou')

contador = 0
while contador < 5:
    print(contador)
    contador += 1