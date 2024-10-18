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

    for navio, tamanho in tamanhos.items():
        while True:
            print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if navio != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal > "))
                orientacao_str = "vertical" if orientacao == 1 else "horizontal"
            else:
                orientacao_str = "vertical"  # Submarino não precisa de orientação

            if posicao_valida(frota, linha, coluna, orientacao_str, tamanho):
                preenche_frota(frota, navio, linha, coluna, orientacao_str, tamanho)
                break
            else:
                print("Esta posição não está válida!")

    print(frota)


main()