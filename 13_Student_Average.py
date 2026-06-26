import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------
# Vamos imaginar o seguinte problema:

# -> Você precisa de um programa para avaliar a pontuação média dos alunos;
# -> O programa deve solicitar o nome do aluno, seguido de sua pontuação única;
# -> Os nomes podem ser inseridos em qualquer ordem;
# -> Inserir um nome vazio termina a inserção dos dados (obs: inserir uma 
# pontuação vazia gerará a exceção ValueError, mas não se preocupe com isso agora)
# -> Uma lista de todos os nomes, juntamente com a pontuação média avaliada, deve ser emitida.


school_class = {}

while True:
    name = input("Digite o nome do aluno: ")
    if name == '':
        break
 
    score = int(input("Insira a pontuação do aluno (0-10): "))
    if score not in range(0, 11):
        break
 
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
    counter += 1
    print(name, ":", adding / counter)

# Agora, vamos analisá-la linha a linha:

# linha 1....: cria um dicionário vazio para os dados de entrada; o nome do aluno é usado como uma chave, enquanto todas as pontuações associadas são armazenadas em uma tupla (a tupla pode ser um valor de dicionário - isso não é um problema)
# linha 3....: insira um loop "infinito" (não se preocupe, ele vai quebrar no momento certo)
# linha 4....: leia o nome do aluno aqui;
# linha 5-6..: se o nome for uma string vazia (), deixe o loop;
# linha 8....: solicite uma das pontuações do aluno (um número inteiro entre 0 e 10)
# linha 9-10.: se a pontuação inserida não estiver dentro do intervalo de 0 a 10, deixe o loop;
# linha 12-13: se o nome do aluno já estiver no dicionário, aumente a tupla associada à nova pontuação (observe o operador + =)
# linha 14-15: se este é um novo aluno (desconhecido para o dicionário), crie uma nova entrada - seu valor é uma tupla de um elemento que contém a pontuação inserida;
# linha 17...: itera os nomes dos alunos classificados;
# linha 18-19: inicialize os dados necessários para avaliar a média (soma e contador)
# linha 20-22: iteramos pela tupla, pegando todas as pontuações subsequentes e atualizando a soma, juntamente com o contador;
# linha 23...: avaliar e imprimir o nome do aluno e a pontuação média.