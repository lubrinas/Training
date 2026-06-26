import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

my_tuple = (1, 10, 100, 1000)
# my_tuple = tuple((1, 10, 100, 1000)) -> tuple() é a função para transformar listas em tuplas
# my_tuple = tuple() -> para declaração de uma tupla vazia

# Tuplas possuem os mesmos mecanismos de leitura de Listas,
# porém não podem ser modificadas. Somente lidas.
print('Elemento 0.............:',my_tuple[0])
print('Elemento -1............:',my_tuple[-1])
print('Elementos 1 ao final...:',my_tuple[1:])
print('Elementos 0 ao -2......:',my_tuple[:-2])

print('Tupla completa:')
for elem in my_tuple:
    print(elem)
print('___________________________________________\n')
# Outras operações e funçôes possíveis com Tuplas
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print('Length ------------------------>',len(t2))
print('t1 = my_tuple + (1000, 10000) ->',t1)
print('t2 = my_tuple * 3 ------------->',t2)
print('10 in my_tuple ---------------->',10 in my_tuple)
print('-10 not in my_tuple ----------->',-10 not in my_tuple)

print('___________________________________________\n')
# Outras operações e funçôes possíveis com Tuplas
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
print('t1, t2, t3:',t1, t2, t3,'\n')
 
t1, t2, t3 = t2, t3, t1
print('t1, t2, t3 = t2, t3, t1:')
print('t1, t2, t3:',t1, t2, t3)