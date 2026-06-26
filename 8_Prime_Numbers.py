import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

import math

def is_prime(num):
    # Um número primo é maior que 1.
    if num <= 1:
        return False
    
    # Tentamos dividir por todos os números começando em 2.
    # Otimização: Só precisamos verificar até a raiz quadrada do número (num**0.5).
    # Se num tem um divisor maior que sua raiz, também terá um menor.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False # Encontrou um divisor, não é primo
            
    return True # Não encontrou divisores, é primo

# Teste da função com os números de 1 a 20 (para cobrir a saída esperada)
for i in range(1, 20):
    if is_prime(i):
        print(i, end=" ")

# Saída esperada: 2 3 5 7 11 13 17 19