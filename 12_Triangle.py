import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

# Programa que define se 3 medidas formam um triângulo,
# mostra sua área, usando a Fórmula de Heron: 
# ÁREA = raíz {p(p-a)(p-b)(p-c)} onde p é o semiperímetro: p = (a +b + c) / 2
# E ainda mostra se é um Triângulo de Ângulo Reto usando o Teorema de Pitágoras:
# c² = a² + b²

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
  
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
print('Área de um triângulo de lados: 1., 1. e 2. ** .5 ->',area_of_triangle(1., 1., 2. ** .5))
print('As medidas 5, 3 e 4 formam um triângulo?',is_a_right_triangle(5, 3, 4))
print('As medidas 1, 3 e 4 formam um triângulo?',is_a_right_triangle(1, 3, 4))