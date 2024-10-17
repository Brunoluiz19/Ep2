def define_posicoes(linha, coluna, orientacao, tamanho): #Ex1
    posicoes = []

    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho): #Ex2
    pos = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota.keys():
        frota[navio].append(pos)
    else:
        frota[navio] = [pos]

    return frota

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

def afundados(frota, tabuleiro):
    
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

    posicoes = define_posicoes(linha, coluna, orientacao< tamanho)

    for linha_pos, coluna_pos in posicoes:
        if not (0 <= linha_pos < 10) or not (0 <= coluna_pos < 10):
            return False
    
    for navios in frota.values():
        for navio in navios:
            for posicao_ocupada in navio:
                if posicao_ocupada in posicoes:
                    return False
                
    return True 
