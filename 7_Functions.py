import os
# Limpa o terminal, independente se é Windows ou Linux/Mac
os.system('cls' if os.name == 'nt' else 'clear')
#--------------------------------------------------------------

def is_year_leap(year):
    """Retorna True se o ano for bissexto, False caso contrário."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    """Retorna o número de dias em um mês específico de um ano."""
    if month < 1 or month > 12:
        return None
    
    # Meses com 31 dias
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Meses com 30 dias
    elif month in [4, 6, 9, 11]:
        return 30
    # Fevereiro
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    return None

def day_of_year(year, month, day):
    """ Retorna o dia correspondente do ano (1-366) ou None se a data for inválida."""
    # 1. Valida o mês
    if month < 1 or month > 12:
        return None
    
    # 2. Valida o dia usando a função days_in_month
    max_days = days_in_month(year, month)
    if day < 1 or day > max_days:
        return None
    
    # 3. Calcula o dia do ano
    day_count = 0
    for m in range(1, month):
        day_count += days_in_month(year, m)
    
    day_count += day
    return day_count

# --- Casos de Teste ---
print("--- Testes Funcionais ---")
print(day_of_year(2000, 12, 31))  # Esperado: 366 (Bissexto)
print(day_of_year(2023, 1, 1))    # Esperado: 1
print(day_of_year(2023, 3, 1))    # Esperado: 60 (31 jan + 28 fev + 1 mar)
print(day_of_year(2024, 3, 1))    # Esperado: 61 (31 jan + 29 fev + 1 mar - bissexto)

print("\n--- Testes de Validação (Esperado: None) ---")
print(day_of_year(2023, 2, 29))   # Fev 2023 não tem 29
print(day_of_year(2023, 13, 1))   # Mês inválido
print(day_of_year(2023, 4, 31))   # Abril só tem 30
print(day_of_year(2023, 1, 0))    # Dia zero é inválido