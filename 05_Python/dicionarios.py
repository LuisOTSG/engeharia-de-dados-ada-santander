# Aula 12 - Dicinários

# Criando dicionários
dict = {}
# dict2 = dict()
dict3 = {'Nome': 'Luis', 'Idade': 25, 'Altura': 1.72}

print(dict3)
print(dict3['Idade'])

# Adicionando elementos em um dicionário
dict3['Função'] = True
print(dict3)

dict3['Função'] = 'Programador'
print(dict3)

# Iterando sobre um dicionário
for chave in dict3: # Por default percorre as chaves
    print(chave, dict3[chave])

# Testando a existência de uma chave
print('Peso' in dict3)
print('Altura' in dict3)