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

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0 for i in range(10)] for i in range(10)]
    for info in frota.values():
        for navio in info:
            for pos in navio:
                [linha, coluna] = pos
                tabuleiro[linha][coluna] = 1
    return tabuleiro