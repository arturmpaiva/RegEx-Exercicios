import re
numeros = ["123", "-45", "3.14", "0.5", "-.9", "-10.0", "abc", "12."]

# inteiros
padraoInteiros = r"^-?\d+(\.0*)?$"

# reais
padraoReais = r"^-?\d*\.?\d+$"

for identificador in numeros:
    if re.fullmatch(padraoInteiros, identificador):
        print(f"{identificador} é um inteiro válido")

# Verificando números reais
for identificador in numeros:
    if re.fullmatch(padraoReais, identificador):
        print(f"{identificador} é um número real válido")