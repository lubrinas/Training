import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

# 1. Peça ao usuário para inserir uma palavra
user_word = input("Digite uma palavra: ")

# 2. Converta a palavra inserida pelo usuário em maiúsculas
user_word = user_word.upper()
word_without_vowels = ""

# 3. Use um loop for para percorrer a palavra
for letter in user_word:
    # 4. Use execução condicional e continue para "consumir" as vogais
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    # 5. Imprima as letras não consumidas
    print(letter)
    word_without_vowels += letter

print(word_without_vowels)
