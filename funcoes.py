def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    pos = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota.keys():
        frota[navio].append(pos)
    else:
        frota[navio] = [pos]

    return frota