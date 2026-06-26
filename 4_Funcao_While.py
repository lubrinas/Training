import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

import time

for i in range(1,6):
    print(i,"Mississipi!")
    time.sleep(1)

print('Pronto ou não, aqui vou eu!')