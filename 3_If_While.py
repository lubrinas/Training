import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

n = int(input("Digite um número inteiro: ")) 
print('O número',n,'é maior ou igual a 100?',n >= 100)

if n >= 100:
    i = 100
    while i <= n:
        print(i)
        i += 1


# n <  100  -> false
# n >= 100  -> true