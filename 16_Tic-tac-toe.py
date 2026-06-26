import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

from random import randrange

def display_board(board):
    # A função aceita um parâmetro contendo o status atual do tabuleiro
    # e o imprime no console com o formato específico solicitado.
    for row in range(3):
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre seu movimento, 
    # verifica a entrada e atualiza o tabuleiro de acordo com a decisão do usuário.
    while True:
        try:
            move = int(input("Digite seu movimento (1-9): "))
            if move < 1 or move > 9:
                print("Erro: Digite um número entre 1 e 9.")
                continue
            
            # Converte o número 1-9 para índices de linha e coluna
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            # Verifica se o campo está ocupado (se não é um número, é 'X' ou 'O')
            if board[row][col] in ['X', 'O']:
                print("Campo já ocupado! Tente outro.")
                continue
            
            board[row][col] = 'O'
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

def make_list_of_free_fields(board):
    # A função navega no tabuleiro e cria uma lista de todos os quadrados vazios.
    # A lista é composta por tuplas, onde cada tupla é um par de números de linha e coluna.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # A função analisa o status do tabuleiro para verificar se 
    # o jogador que utiliza 'O's ou 'X's ganhou o jogo.
    
    # Verifica linhas e colunas
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)): return True # Linha
        if all(board[j][i] == sign for j in range(3)): return True # Coluna
    
    # Verifica diagonais
    if all(board[i][i] == sign for i in range(3)): return True
    if all(board[i][2-i] == sign for i in range(3)): return True
    
    return False

def draw_move(board):
    # A função desenha o movimento do computador e atualiza o tabuleiro.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        # Escolhe um índice aleatório da lista de campos livres
        choice = randrange(len(free_fields))
        row, col = free_fields[choice]
        board[row][col] = 'X'

# --- Lógica Principal do Jogo ---

# Inicializa o tabuleiro com os números de 1 a 9
board = [[(i * 3 + j + 1) for j in range(3)] for i in range(3)]

# O primeiro movimento pertence ao computador: 'X' no meio (posição 5)
board[1][1] = 'X'
display_board(board)

while True:
    # Vez do Usuário
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("Você ganhou!")
        break
    if not make_list_of_free_fields(board):
        print("Empate!")
        break

    # Vez do Computador
    print("Vez do computador...")
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("O computador ganhou!")
        break
    if not make_list_of_free_fields(board):
        print("Empate!")
        break