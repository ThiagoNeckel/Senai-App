
linhas = 20
tamanho = linhas * 2 - 1
espacos = (tamanho - 1) / 2
i = 1

while i <= linhas:
    print(" " * (espacos - i + 1))
    print("*" * (2 * i - 1))
    i =+ 1;