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
        
        if navio == "porta-aviões":
            quantidade = 1
        elif navio == "navio-tanque":
            quantidade = 2
        elif navio == "contratorpedeiro":
            quantidade = 3
        elif navio == "submarino":
            quantidade = 4

        
        for _ in range(quantidade):
            print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
            while True:
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))

                
                if navio == "submarino":
                    orientacao = "horizontal"
                else:
                    orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                    orientacao = "vertical" if orientacao_input == 1 else "horizontal"

                
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    
                    preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
                    break
                else:
                    print("Esta posição não está válida!")

    print(frota)


main()