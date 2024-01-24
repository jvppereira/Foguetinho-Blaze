import random

def print_color(message, color):
    colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'blue': '\033[94m',
            'reset': '\033[0m'
    }
    print(colors[color] + message + colors['reset'])
print("")
print_color(" ---- SIMULADOR DO JOGO DO FOGUETINHO DA BLAZE ---- ", 'red')
print("")
print_color(" * Esse simulador gera valores aleátorios para a aposta de cada player de 1 a 1000 R$ sem um parametro para o desvio padrao desses valores, portanto os resultados não refletem valores reais. ", 'blue')
print("")
n = int(input("Digite quantas rodadas quer simular (exemplo: 10): "))

def loop(n):
    taxa = float(input("Digite a taxa de retorno padrão por rodada (exemplo: 20): "))
    taxa = taxa/100
    b = int(input("Digite o valor máximo de players que vão jogar por rodada (exemplo: 100): "))
    medialp = []
    mult = []
    mediag = []
    mediap = []
    medial = []

    for p in range(0, n):
        def generate_random_data(num_values):
            valores = [random.randint(1, 1000) for _ in range(num_values)]
            nomes = ["Player" + str(i) for i in range(1, num_values + 1)]
            return valores, nomes

        def blaze(valores, multiplicador, players, taxa):
            quebrou = False
            taxan = 1 - taxa
            totalbruto = sum(valores)
            capital_inicial = taxan * totalbruto
            lucroblaze = 0
            perdas_jogadores = {player: 0 for player in players}
            vencedores = []
            perdedores = []

            while not quebrou and len(valores) > 1:
                jogador_removido = random.choice(range(len(valores)))
                ganhos_jogador = valores[jogador_removido] * multiplicador
                lucroblaze += ganhos_jogador - valores[jogador_removido]

                if perdas_jogadores[players[jogador_removido]] == 0:
                    perdas_jogadores[players[jogador_removido]] = -valores[jogador_removido]
                    vencedores.append(players[jogador_removido])
                else:
                    perdas_jogadores[players[jogador_removido]] -= valores[jogador_removido]
                    perdedores.append(players[jogador_removido])

                capital_inicial -= valores[jogador_removido]
                valores.pop(jogador_removido)

                if capital_inicial > 0:
                    multiplicador += 0.01
                    print("Valor do foguetinho:", multiplicador)
                    print("---------------")
                    #for i in range(len(valores)):
                        #print(f"{players[i]} tem {valores[i]}")

                    print(f"{players[jogador_removido]} saiu e ganhou {ganhos_jogador}")
                else:
                    quebrou = True
                    print("Foguetinho quebrou em: ",multiplicador )
                    mult.append(multiplicador)

            lucroblaze += capital_inicial
            print("---------------")
            print("Total de jogadores da rodada:", len(players))
            print("Total de vencedores da rodada:", len(vencedores))
            print("Total de perdedores da rodada:", len(perdedores))

            #print("---------------")
            #print("Vencedores da rodada:", vencedores)
            #print("Perdedores da rodada:", perdedores)
            print("---------------")
            print("Total da rodada:", totalbruto)
            taxaretorno = (lucroblaze / totalbruto) * 100
            print("Lucro da casa de apostas Blaze:", lucroblaze, ". ", taxaretorno, "%", " Em relação ao total investido. ")
            print("---------------")

            medialp.append(taxaretorno)
            medial.append(lucroblaze)
            mediag.append(len(perdedores))
            mediap.append(len(vencedores))

            for player, perda in perdas_jogadores.items():
                if perda < 0:
                    print(f"- {player} perdeu {abs(perda)}")

        multiplicador = 1
        valordeplayers = random.randint(1, b)
        valores_simulacao, players_simulacao = generate_random_data(valordeplayers)

        blaze(valores_simulacao, multiplicador, players_simulacao, taxa)

    # ...

    print("--------------------------------")
    print_color("Média de percentual de lucro (%): ", 'green'), print(sum(medialp) / len(medialp), "%")
    print("--------------------------------")
    print_color("Média de lucro por rodada (R$): ", 'green'), print(sum(medial) / len(medial), "R$")
    print("--------------------------------")
    print_color("Média de ganhadores por rodada: ", 'green'), print(int(sum(mediag) / len(mediag)))
    print("--------------------------------")
    print_color("Média de perdedores por rodada: ", 'red'), print(int(sum(mediap) / len(mediap)))
    print("--------------------------------")
    print_color("Média de crash do multiplicador: ", 'blue'), print(sum(mult) / len(mult))
    print("--------------------------------")

loop(n)
