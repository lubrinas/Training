import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

# entre com um valor float para a variável a aqui
a = float(input('Digite a = '))
# entre com um valor float para a variável b aqui
b = float(input('Digite b = '))
print('')

# imprima o resultado da adição aqui
print('Adição a + b = ', a + b)
# imprima o resultado da subtração aqui
print('Subtração a - b = ', a - b)
# imprima o resultado da multiplicação aqui
print('Multiplicação a * b = ', a * b)
# imprima o resultado da divisão aqui
print('Divisão a / b = ', a / b)
print("\nIsso é tudo, pessoal!")