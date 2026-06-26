import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

# Dicionários são como listas casadas. O primeiro elemento fuciona como índice do 2º
# novo_dict = dict() -> é a função para criar um dicionário vazio
# pessoa = dict(nome = "Ana", idade = 25) -> {'nome': 'Ana', 'idade': 25}
# pares = [("a", 1)("b", 2)] -> meu_dict = dict(pares)

dictionary = {
                "gato" : "chat",
                "cachorro" : "chien",
                "cavalo" : "cheval"
            }
phone_numbers = {
                    'chefe' : 5551234567,
                    'Suzy' : 22657854310
                }
empty_dictionary = {}

print('Dicitionary.............:',dictionary)
print('Dicitionary["gato"].....:',dictionary['gato'])
print('phone_numbers["Suzy"]...:',phone_numbers['Suzy'])
print('___________________________________________\n')

dictionary = {
                "gato": "chat",
                "cachorro": "chien",
                "cavalo": "cheval"
            }
words = ['gato', 'lion', 'cavalo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")
print('___________________________________________\n')

# Acessando pelo método keys() que retorna todas as chaves do dicionário
# Ter um grupo de chaves permite acessar todo o dicionário de forma fácil e prática.
print('Acessando pelo método KEYS():')
for key in dictionary.keys():
    print(key, "(chave) ->", dictionary[key])
print('___________________________________________\n')

# Acessando pelo método items() que retorna tuplas em que cada tupla é um par de valores-chave.
print('Acessando pelo método ITEMS():')
for pares in dictionary.items(): # Repare que a variável pares é uma tupla
    print(pares)
print('___________________________________________\n')

print('Acessando pelo método ITEMS(), agora pegando cada item da tupla:')
for english, french in dictionary.items(): # Agora english e french pegam cada item da tupla
    print(english, "->", french)
print('___________________________________________\n')

print('Usando SORTED() para printar em ordem o dicionário pelas chaves:')
print(sorted(dictionary.keys()))
print(dictionary.keys()) # Repare q sorted() não reorganiza dictionary{}. Apenas ordena no print.
print('___________________________________________\n')

# Se quiser fazer uma modificação, usar a chave como índice e o par será modificado.
# dictionary['gato'] = 'minou'
# print(dictionary) # printa 'minou' no lugar de 'chat' como par te 'gato'
# print('___________________________________________\n')

# É possível ainda acrescentar um novo par no dicionário. É só atribuir um valor a uma chave inexistente.
print('Acrescentando o par "swan":"cygne" ao dicionário:')
dictionary['swan'] = 'cygne' 
print(dictionary,'\n') # Repare q 'swan' : 'cygne' foi acrescido ao final do dicionário

print('Acrescentando o par "swan":"cygne" ao dicionário agora usando o método update():')
dictionary.update({"pato": "canard"})
print(dictionary)
print('___________________________________________\n')

# Removendo uma chave (um par) do dicionário usando del:
# OBS: remover uma chave não existente causa um erro.
print('Removendo o par pela key "cachorro":')
del dictionary['cachorro']
print(dictionary,'\n')

print('Removendo o último item do dicionário pelo método popitem():')
dictionary.popitem() # Remove o último par do dicionário. Antes da versão 3.6.7, o método popitem() removia um item aleatório de um dicionário.
print(dictionary)
print('___________________________________________\n')


my_dictionary = {"A": 1, "B": 2}
print('Antes: my_dictionary ->',my_dictionary)

copy_my_dictionary = my_dictionary.copy() # usando o método copy () para salvar o dicionário q será apagado
print('Apagando usando o método clear()...\n')
my_dictionary.clear() # limpa todos os dados do dicionário

print('Depois: my_dictionary ->',my_dictionary)
print('Nova: copy_my_dictionary ->',copy_my_dictionary)