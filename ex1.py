import re
identificadores = ["variavel1", "_invalido", "a123", "muitoLongoIdentificadorQueNaoDeveSerValido", "x", "outro_valido"]

padrao = r"^[a-zA-Z][a-zA-Z0-9_]{1,14}$"

for identificador in identificadores:
    validos = re.findall(padrao, identificador)
    print(f"Identificadores válidos: {validos}")