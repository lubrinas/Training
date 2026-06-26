import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

secret_number = 777

print("""
+===================================+
| Bem-vindo ao meu jogo, trouxa!    |
| Insira um número inteiro e ten-   |
| te adivinhar o número que tenho   |
| escolhido para você!!!            |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input('Digite seu número: '))

while number != secret_number:
    print(number,'não é o número que escolhi, bobão!\n')
    number = int(input('Digite um outro número : '))

print('Nossa... FINALMENTE vc advinhou. O número correto é ', number,'.', sep="")