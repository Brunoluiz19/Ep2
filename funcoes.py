def define_posicoes(linha, coluna, orientacao, tamanho): #Ex1
    posicoes = []

    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            posicoes.append([linha, coluna + i])
        else:  
            posicoes.append([linha + i, coluna])
    frota[navio].append(posicoes)

def faz_jogada(tabuleiro, linha, coluna): #Ex3
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota): #Ex4
    tabuleiro = [[0 for i in range(10)] for i in range(10)]
    for info in frota.values():
        for navio in info:
            for pos in navio:
                [linha, coluna] = pos
                tabuleiro[linha][coluna] = 1
    return tabuleiro

def afundados(frota, tabuleiro):#Ex5
    
    n_tam = {
        "porta-aviões": 4,
        "navio-tanque": 3,
        "contratorpedeiro": 2,
        "submarino": 1
    }

    n_afundas = 0
    for navio, pos in frota.items():
        x_tam = n_tam[navio]

        for n in pos:
            x = []

            for coord in n:
                [linha, coluna] = coord
                x.append(tabuleiro[linha][coluna])

            if all(estado == "X" for estado in x):
                n_afundas += 1
    return n_afundas

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    if orientacao == "horizontal":
        if coluna + tamanho > 10:  
            return False
        for i in range(tamanho):
            if any([linha == x[0] and coluna + i == x[1] for navio in frota.values() for x in navio]):
                return False  
    else:  
        if linha + tamanho > 10: 
            return False
        for i in range(tamanho):
            if any([linha + i == x[0] and coluna == x[1] for navio in frota.values() for x in navio]):
                return False  
    return True

