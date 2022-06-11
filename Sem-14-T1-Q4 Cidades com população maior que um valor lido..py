def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado



cidades = carrega_cidades()
maior = int(input().strip())
print(f'CIDADES COM MAIS DE {maior} HABITANTES:')

# se a população da cidade for maior que o número digitado mostrar na tela.
for i in cidades:
    if i[5] > maior:
        print(f'IBGE: {i[1]} - {i[2]}({i[0]}) - POPULAÇÃO: {i[5]}')
