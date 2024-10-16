def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes


linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))