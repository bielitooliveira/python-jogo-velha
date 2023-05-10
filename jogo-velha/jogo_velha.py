from random import randint #importar funcoes de bibliotecas
from time import sleep

casas = [] #criar array para armazenar casas escolhidas
casas_preenchidas = [1, 2, 3, 4, 5, 6, 7, 8, 9] #criar array para preencher os valores pelas opcoes usadas

print('JOGO DA VELHA') #exibir na tela
sleep(1) #aguardar por 1 segundo

jogo_velha = """-------
|1|2|3|
-------
|4|5|6|
-------
|7|8|9|
-------"""
print(jogo_velha) #exibir o quadro do jogo da velha

sleep(1)
while True: #criar estrutura de repeticao para fazer a validacao de opcao
    jogador = input('Selecione X ou O: ').upper() #capturar o valor digitado pelo jogador, e o mesmo fica em letra maiscula
    if(jogador == 'X' or jogador == 'O'): #condicao para verificar o que foi digitado
        break #quebrar o looping
vez_jogador = 1 #variavel que fara com que o jogador inicie a partida e haja a revezao de jogo

print(f'O jogador selecionou {jogador}.') #exibir a opcao selecionada
if jogador == 'X': #se o jogador escolher uma opcao, o computador escolhera a outra
    computador = 'O'
else:
    computador = 'X'

sleep(1)
print(f'O computador selecionou {computador}.')

while True:
    if casas_preenchidas[0] == casas_preenchidas[1] == casas_preenchidas[2] or casas_preenchidas[3] == casas_preenchidas[4] == casas_preenchidas[5] or casas_preenchidas[6] == casas_preenchidas[7] == casas_preenchidas[8] or casas_preenchidas[0] == casas_preenchidas[3] == casas_preenchidas[6] or casas_preenchidas[1] == casas_preenchidas[4] == casas_preenchidas[7] or casas_preenchidas[2] == casas_preenchidas[5] == casas_preenchidas[8] or casas_preenchidas[0] == casas_preenchidas[4] == casas_preenchidas[8] or casas_preenchidas[2] == casas_preenchidas[4] == casas_preenchidas[6]:
        break
    else:
        if vez_jogador == 1: #verificar o valor da variavel, e dependendo ou o jogador ou o computador jogara
                sleep(1)
                while True: #criar estrutura de repeticao para evitar opcoes repetidas
                    espaco = int(input('VEZ DO JOGADOR - SELECIONE UM ESPAÇO: ')) #variavel que corresponde a casa do jogo escolhida
                    if(casas.count(espaco) == 0): #verificar a contagem de valores da array casas, pegando o valor da variavel, e se nao houver repeticao, quebre o looping
                        break
                for casa in casas_preenchidas: #criar estrutura de repeticao para percorrer os valores da array casas_preenchidas
                    if espaco == casa: #comparar cada um dos valores da array com o valor da variavel espaco, e se o valor da variavel for igual ao valor na array
                        casas_preenchidas[casa-1] = jogador #substituir o valor da array pela opcao selecionada
                jogo_velha = jogo_velha.replace(str(espaco), jogador) #substituir o numero do quadro do jogo da velha pela opcao selecionada
                casas.append(espaco) #adicionar a array casas o valor do espaco, para posteriormente realizar a contagem de valores
                vez_jogador = 0 #atribuir o valor a variavel, e com a reinicializacao do looping e verificacao do valor fara com que haja mudanca entre jogador e computador
        else: #secao destinada a vez do computador
            sleep(1)
            print('VEZ DO COMPUTADOR - SELECIONE UM ESPAÇO: ')
            while True:
                espaco = randint(1, 9) #fazer com que haja escolha aleatoria da casa
                if(casas.count(espaco) == 0):
                    break
            for casa in casas_preenchidas:
                if espaco == casa:
                    casas_preenchidas[casa-1] = computador
            jogo_velha = jogo_velha.replace(str(espaco), computador)
            casas.append(espaco)
            vez_jogador = 1
        sleep(1)
        print(jogo_velha)

if vez_jogador == 0: #exibir os resultados
    print(f'O JOGADOR VENCEU COM {jogador}!')
else:
    print(f'O COMPUTADOR VENCEU COM {computador}!')