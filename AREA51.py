meuArquivo = open('config.txt', 'r')
bandas = meuArquivo.readlines()

for banda in bandas:
    banda = banda.rstrip('\n')
    print(banda)

print(bandas)
meuArquivo.close()