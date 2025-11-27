with open('teste.txt', 'r') as arquivo:
    linha = arquivo.readline()
    while linha:
        print(linha)
        linha = arquivo.readline()

with open('teste.txt', 'a') as arquivo:
    arquivo.write('\nis(Rael)')