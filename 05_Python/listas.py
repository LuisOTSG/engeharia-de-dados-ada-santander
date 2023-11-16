# Aula 9 - Estrutura de Listas

# Utilizando variáveis
nota1 = 7.8
nota2 = 9.7
nota3 = 8.5

# Utilizando listas
notas = [7.8, 9.7, 8.5]

# Criando lista vazia
lista = []
lista2 = list()
lista3 = [25, 'Luis', 3.14, True]
lista_de_listas = [[1, 2, 3], [5, 10, 20], 100,]

# Indexação
lista = [True, 3.14, 'Luis', 25]

# Acessando a partir do índice
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Acessando de trás pra frente
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Slicing (fatiamento)
lista = [10, 30, 50, 70, 90, 100, 200]

print(lista[0:3])
print(lista[3:7])
print(lista[3:])
print(lista[2:6:2])

# Iteração de listas com FOR
# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
print('Comprimento da lista:', len(lista))
for indice in range(len(lista)):
    print(lista[indice])

# Aula 10 - Métodos e Funções de Listas

lista = [1, 3, 5, 7, 9]
print('Lista antes das funções:', lista)

# Métodos de Listas

# append() - Adiciona elemento (no final)
lista.append(11)
print('Lista com append:', lista)

# insert() - Adiciona elemento (em posição especificada)
lista.insert(2, 4)
print('Lista com insert:', lista)

# extend() - Juntar duas listas
lista2 = [2, 4, 6, 8]
lista.extend(lista2)
print('Lista com extend:', lista)

# pop() - Remover elemento (o último por default ou o índice especificado)
lista.pop()
print('Lista com pop:', lista)

lista.pop(0)
print('Lista com pop com índice:', lista)

# remove() - Remove o primeiro elemento especificado (não é o índice)
lista.remove(3)
print('Lista com remove:', lista)

# count() - Contar elementos especificados
print('Quantidade de números 4:', lista.count(4))

# index() - Indica o índice de um elemento especificado
print('Índice do elemento 6:', lista.index(6))

# sort() - Ordena a lista
lista.sort()
print('Lista ordenada crescente:', lista)
lista.sort(reverse=True)
print('Lista ordenada descrescente:', lista)

# Funções de Listas

# len() - Tamanho da lista
print('Tamanho da lista:', len(lista))

# sum() - Soma dos elementos da lista
print('Soma dos elementos da lista:', sum(lista))

# max() - Maior elemento da lista
print('Maior elemento da lista:', max(lista))

# min() - Menor elemento da lista
print('Menor elemento da lista:', min(lista))