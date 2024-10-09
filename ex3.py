import re
strings = ['"Hello, World!"', '"Linha\ninvalida"', '"Escaped \\"Quote\\""', '"Unterminated string', '""']

padrao = r'"([^"\n]*(\\"[^"\n]*)*)"'

for string in strings:
    if re.fullmatch(padrao, string):
        print(f'{string} é uma string literal válida')
    else:
        print(f'{string} não é uma string literal válida')