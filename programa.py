from funcoes import define_posicoes, preenche_frota, posicao_valida

def main():
    
    frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": []
    }

    
    navios_info = {
        "porta-aviões": 4,
        "navio-tanque": 3,
        "contratorpedeiro": 2,
        "submarino": 1
    }

    
    for navio, tamanho in navios_info.items():
        quantidade = 5 - tamanho  
        for _ in range(quantidade):
            while True:
                print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
                
                
                if navio != "submarino":
                    orientacao = int(input("[1] Vertical [2] Horizontal > "))
                    orientacao_str = "vertical" if orientacao == 1 else "horizontal"
                else:
                    orientacao_str = "vertical"  


                if posicao_valida(frota, linha, coluna, orientacao_str, tamanho):
                    preenche_frota(frota, navio, linha, coluna, orientacao_str, tamanho)
                    break
                else:
                    print("Esta posição não está válida!")

    
    
    frota_oponente = {
        'porta-aviões': [
            [[9, 1], [9, 2], [9, 3], [9, 4]]
        ],
        'navio-tanque': [
            [[6, 0], [6, 1], [6, 2]],
            [[4, 3], [5, 3], [6, 3]]
        ],
        'contratorpedeiro': [
            [[1, 6], [1, 7]],
            [[0, 5], [1, 5]],
            [[3, 6], [3, 7]]
        ],
        'submarino': [
            [[2, 7]],
            [[0, 6]],
            [[9, 7]],
            [[7, 6]]
        ]
    }


    def posiciona_frota(frota):
        
        pass

    def faz_jogada(tabuleiro, linha, coluna):
        
        pass

    def afundados(frota, tabuleiro):
        
        pass

    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto


    tabuleiro_oponente = posiciona_frota(frota_oponente)
    tabuleiro_jogador = posiciona_frota(frota)

    
    jogando = True
    jogadas_realizadas = set()  

    
    while jogando:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        
        
        while True:
            try:
                linha = int(input("Jogador, qual linha deseja atacar? "))
                if 0 <= linha <= 9:
                    break
                else:
                    print("Linha inválida!")
            except ValueError:
                print("Linha inválida!")


        while True:
            try:
                coluna = int(input("Jogador, qual coluna deseja atacar? "))
                if 0 <= coluna <= 9:
                    break
                else:
                    print("Coluna inválida!")
            except ValueError:
                print("Coluna inválida!")

        
        if (linha, coluna) in jogadas_realizadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
            continue
        
        
        jogadas_realizadas.add((linha, coluna))

        
        faz_jogada(tabuleiro_oponente, linha, coluna)

        
        if afundados(frota_oponente, tabuleiro_oponente):
            print("Parabéns! Você derrubou todos os navios do seu oponente!")
            jogando = False


main()