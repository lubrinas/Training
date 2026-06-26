import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

def liters_100km_to_miles_gallon(liters):
    # 1. Converter l/100km para litros por metro: liters / 100000
    # 2. Converter litros por metro para galões por metro: (liters / 100000) / 3.785411784
    # 3. Converter galões por metro para galões por milha: ((liters / 100000) / 3.785411784) * 1609.344
    # 4. Inverter para ter milhas por galão: 1 / passo_3
    
    km_por_litro = 100 / liters
    milhas_por_km = 1 / 1.609344
    galoes_por_litro = 1 / 3.785411784
    
    # Formula direta derivada:
    mpg = (100 * 3.785411784) / (1.609344 * liters)
    return 1 / ( (liters / 100) * (3.785411784 / 1609.344) ) # Alternativa
    # Usando a fórmula direta mais simples baseada nas conversões fornecidas:
    return 235.214583 / liters

def miles_gallon_to_liters_100km(mpg):
    # Formula direta: 100 litros / (mpg * 1.609344 km/milha) * 3.785411784 L/galão
    l_100km = (100 * 3.785411784) / (1.609344 * mpg)
    return l_100km

# Testes
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))