from random import randint #importar funcoes de bibliotecas
from time import sleep

casas = [1, 2, 3, 4, 5, 6, 7, 8, 9] #criar array para substituir os valores
vez_jog = -1 #criar variavel para iniciar a partida e revezar o jogo

print('JOGO DA VELHA') #exibir o titulo
sleep(0.8) #aguardar por 0.8 segundo

lin1_col1 = lin1_col2 = lin1_col3 = lin2_col1 = lin2_col2 = lin2_col3 = lin3_col1 = lin3_col2 = lin3_col3 = '| ' #variaveis para formar o jogo e substituir os valores

while True: #manter o jogo ate o jogador/robo vencer
    jogo = '   1 2 3\n' + '  ------- \n1 ' + lin1_col1 + lin1_col2 + lin1_col3 + '|\n  ------- \n2 ' + lin2_col1 + lin2_col2 + lin2_col3 + '|\n  ------- \n3 ' + lin3_col1 + lin3_col2 + lin3_col3 + '|\n  -------' #criar e modificar o tabuleiro
    print(jogo) #exibir o tabuleiro

    if casas[0] == casas[1] == casas[2] \
    or casas[3] == casas[4] == casas[5] \
    or casas[6] == casas[7] == casas[8] \
    or casas[0] == casas[3] == casas[6] \
    or casas[1] == casas[4] == casas[7] \
    or casas[2] == casas[5] == casas[8] \
    or casas[0] == casas[4] == casas[8] \
    or casas[2] == casas[4] == casas[6]: #verificar se houve condicoes de vitoria
        break #quebrar caso afirmativo
    
    else: #manter o jogo caso negativo
        sleep(0.8)
        if vez_jog == -1: #verificar se houve as definicoes iniciais de jogo e dos simbolos de cada um. fazer as definicoes iniciais caso nao houve
            while True: #manter a validacao de opcao
                jogador = input('SELECIONE X OU O: ') #capturar o valor do jogador
                if(jogador != '' and jogador.upper().strip()[0] in 'XxOo'): #verificar se o valor nao foi um enter e tornar maiusculo, remover espacos pegar o primeiro char
                    jogador = jogador.upper().strip()[0]  #modificar e atribuir a mesma variavel o seu valor em maisculo, sem espacos e com apenas o seu primeiro char
                    break #quebrar o looping
                else:
                    print('VALOR INVÁLIDO... DIGITE X OU O') #exibir mensagem de erro e repetir o looping caso negativo
            vez_jog = 1 #fazer com que o jogador inicie a partida e haja a revezao de jogo

            print(f'O JOGADOR SELECIONOU {jogador}') #exibir a opcao selecionada
            if jogador == 'X': #se o jogador escolher uma opcao
                robo = 'O' #o computador escolhera outra
            else:
                robo = 'X'

            sleep(0.8)
            print(f'O COMPUTADOR SELECIONOU {robo}')
            sleep(0.8)

        else: #continuar o jogo e a revezao caso ja foi definido o simbolo de cada um
            if vez_jog == 1: #verificar se e a vez do jogador ou do robo
                print('VEZ DO JOGADOR - SELECIONE UM ESPAÇO: ')
            else:
                print('VEZ DO COMPUTADOR - SELECIONE UM ESPAÇO: ')
            while True: #manter a solicitao do valor do jogador/robo e impedir caso houver fornecimento de valor novo
                linha = coluna = 0 #atribuir os valores de linha e coluna para entrar na condicao e resetar na nova iteracao
                if vez_jog == 1: #proceder caso for a vez do jogador
                    while linha < 1 or linha > 3 and coluna < 1 or coluna > 3: #manter a validacao da opcao selecionada
                        linha = input('LINHA: ') #capturar o valor da linha
                        coluna = input('COLUNA: ') #capturar o valor da coluna
                        if linha.isnumeric() and coluna.isnumeric(): #verificar se o valor e um numero
                            linha = int(linha) #transformar de texto para numero as variaveis linha e coluna caso positivo
                            coluna = int(coluna)
                        else: #exibir mensagem de erro e resetar os valores para manter a validacao caso negativo
                            print('VALOR INVÁLIDO... SELECIONE UM NÚMERO: ')
                            linha = coluna = 0
                    if linha == 1: #verificar a linha informada
                        if coluna == 1: #verificar a coluna informada
                            espaco = 1 #e atribuir um valor a variavel espaco
                        elif coluna == 2:
                            espaco = 2
                        elif coluna == 3:
                            espaco = 3
                    elif linha == 2:
                        if coluna == 1:
                            espaco = 4
                        elif coluna == 2:
                            espaco = 5
                        elif coluna == 3:
                            espaco = 6
                    elif linha == 3:
                        if coluna == 1:
                            espaco = 7
                        elif coluna == 2:
                            espaco = 8
                        elif coluna == 3:
                            espaco = 9
                    jogada = jogador #fazer com que a variavel jogada receba o simbolo selecionado
                else: #proceder caso for a vez do robo
                    espaco = randint(1, 9) #fazer com que haja escolha aleatoria da casa
                    jogada = robo
                    
                if casas[espaco-1] != 'X' and casas[espaco -1] != 'O': #verificar se o valor informado pelo jogador/robo nao e repetido. caso nao for
                    break #quebrar o looping de solicitao de valor para jogador/robo

            if espaco == 1: #verificar o valor do espaco
                lin1_col1 = lin1_col1.replace('| ','|'+jogada) #e substituir o texto das variaveis que compoem o tabuleiro e preencher o mesmo pelo sinal do jogador/robo
            elif espaco == 2:
                lin1_col2 = lin1_col2.replace('| ', '|'+jogada)
            elif espaco == 3:
                lin1_col3 = lin1_col3.replace('| ', '|'+jogada)
            elif espaco == 4:
                lin2_col1 = lin2_col1.replace('| ','|'+jogada)
            elif espaco == 5:
                lin2_col2 = lin2_col2.replace('| ', '|'+jogada)
            elif espaco == 6:
                lin2_col3 = lin2_col3.replace('| ', '|'+jogada)
            elif espaco == 7:
                lin3_col1 = lin3_col1.replace('| ','|'+jogada)
            elif espaco == 8:
                lin3_col2 = lin3_col2.replace('| ', '|'+jogada)
            else:
                lin3_col3 = lin3_col3.replace('| ', '|'+jogada)

            casas[espaco-1] = jogada #substituir o valor do elemento da array pelo sinal do jogador/robo e contribuir na estrutura de validacao de valores
            sleep(0.75)

            if vez_jog == 1: #verificar se e a vez do jogador/robo
                vez_jog = 0 #mudar a vez para o robo caso seja positivo
            else:
                vez_jog = 1 #mudar a vez para o jogador caso seja negativo

if vez_jog == 0: #exibir os resultados
    print(f'O JOGADOR VENCEU COM {jogador}!')
else:
    print(f'O COMPUTADOR VENCEU COM {robo}!')