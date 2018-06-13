from random import randint
import time

"Funcoes para facilitar o codigo"
#funcao input() que retorna o texto obtido em caixa-alta
def input_caixa_alta(msg):
    print(msg)
    texto = str(input())
    texto = texto.upper()
    return texto

def temNumeros(inputString):
    return any(char.isdigit() for char in inputString)

#funcao que retorna os numeros de uma string dada
def achar_num(stringDada):
    novaLista = list(stringDada)
    numerosAchados = 0
    strNumeros = '0'
    for cont in range (len(novaLista)):
        if temNumeros(novaLista[cont]) and numerosAchados == 0:
            strNumeros = novaLista[cont]
            numerosAchados += 1
        elif temNumeros(novaLista[cont]) and numerosAchados == 1:
            strNumeros += novaLista[cont]
    return int(strNumeros)

#funcao que retorna as letras de uma string dada
def achar_letra(stringDada):
    novaLista = list(stringDada)
    letrasAchadas = 0
    strLetras = '0'
    for cont in range(len(novaLista)):
        if not temNumeros(novaLista[cont]) and letrasAchadas == 0:
            strLetras = novaLista[cont]
            letrasAchadas += 1
        elif not temNumeros(novaLista[cont]) and letrasAchadas == 1:
            strLetras += novaLista[cont]
    return str(strLetras)

'''funcao que a partir de uma coordenada dada, retorna um array separando letras"
            e numeros da coordenada. Letras em [0], numeros em [1]'''
def array_coordenada(coordenada):
    novaCoordenada = []
    novaCoordenada.append(achar_letra(coordenada))
    novaCoordenada.append(achar_num(coordenada))
    return novaCoordenada

def imprimir_mapa_vazio():
    nLinhas = 20
    nColunas = 20
    matrizDinamica = [""] * nLinhas #cria as linhas do mapa

    for linha in range(nLinhas):
        matrizDinamica[linha] = ["' "] * nColunas #cria as colunas do mapa
        if linha == 0:
            print("   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
        print(chr(linha + 65) + "  " + " ".join(matrizDinamica[linha]))
    return matrizDinamica

def imprimir_mapa(mapa):
    print("   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
    linha = 0
    while linha < nLinhas:
        print(chr(linha + 65) + "  " + " ".join(mapa[linha]))
        linha += 1

"Declaracao de variaveis globais"
nLinhas = 20
nColunas = 20
nFragatas = 0
nPortaAvioes = 0
nCruzadores = 0
fAtingidas = 0
cAtingidos = 0
pAtingidos = 0
linha = 0
pontos = 0

matrizDinamica = [""] * nLinhas #cria as linhas do mapa

"Inicio do codigo"
print("Bem-vindos ao batalha naval de Bruno e Lucas \nEste sera o mapa em que vcs jogarão:")
time.sleep(5)

while linha < nLinhas:
    matrizDinamica[linha] = ["' "] * nColunas #cria as colunas do mapa
    if linha == 0:
        print("   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
    print(chr(linha + 65) + "  " + " ".join(matrizDinamica[linha]))
    linha += 1
mapaP1 = matrizDinamica              #Cria o mapa para posicionamento dos navios a partir da matrizDinamica
mapaP2 = matrizDinamica              #Cria mapa para bombardeamento a partir da matrizDinamica

time.sleep(2)
print("Prontos?\nVamos comecar...")
time.sleep(1)
print("Jogador 2 cubra os olhos, não vale espiar.")
print("Jogador 1 agora vai inserir os barcos no mapa")
time.sleep(4)
while nFragatas < 1 or nCruzadores < 1 or nPortaAvioes < 1:
    escolhaNavio = input_caixa_alta("Insira F se deseja inserir uma fragata, C para cruzador ou P para porta avioes")

    #Posicionar Fragatas
    if escolhaNavio == "F" and nFragatas < 5:
        print("Onde deseja inserir a Fragata?\nApenas letra e número exemplo, A12; T1")
        posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                         " a partir da coordenada dada"))

        #Validacao da coordenada da fragata
        while len(posicaoNavio[0]) != 1 or posicaoNavio[0] > "T" or posicaoNavio[1] >= 20 or\
                posicaoNavio[1] < 1 or\
                mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] != "' " \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1]] != "' ":
            print("coordenada invalida, ou navio já existente na coordenada")
            print("Onde deseja inserir a Fragata?\nApenas letra e número exemplo, A12; T1")
            posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                         " a partir da coordenada dada"))

        #Inserir "F " na casa determinada e na proxima a direita
        for prox in range(-1,1):
            mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + prox] = "F "
        #aumentar o contador de fragatas
        nFragatas += 1
        #imprimir o mapa com o novo barquinho a partir de funcao imprimir_mapa
        imprimir_mapa(mapaP1)

    elif escolhaNavio == "F" and nFragatas >= 5:
        print("Voce ja posicionou todas as 5 fragatas")

    #Posicionar Cruzadores
    elif escolhaNavio == "C" and nCruzadores < 4:
        print("Onde deseja inserir O Cruzador?\nApenas letra e número exemplo, A12; T1")
        posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                         " a partir da coordenada dada"))

        # Validacao da coordenada do Cruzador
        while len(posicaoNavio[0]) != 1 or posicaoNavio[0] > "T" or posicaoNavio[1] >= 19 or \
                posicaoNavio[1] < 1 \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] != "' " \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1]] != "' "\
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + 1] != "' ":
            print("coordenada invalida, ou navio já existente na coordenada")
            print("Onde deseja inserir o Cruzador?\nApenas letra e número exemplo, A12; T1")
            posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                             " a partir da coordenada dada"))

        # Inserir "C " na casa determinada e na proxima a direita
        for prox in range(-1,2):
            mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + prox] = "C "
        #aumentar o contador de Cruzadores
        nCruzadores += 1
        # imprimir o mapa com o novo barquinho a partir de funcao imprimir_mapa
        imprimir_mapa(mapaP1)
    elif escolhaNavio == "C" and nCruzadores >= 4:
        print("Voce ja posicionou todos os 4 Cruzadores")

    #Posicionar Porta-Aviões
    elif escolhaNavio == "P" and nPortaAvioes < 3:
        print("Onde deseja inserir o Porta-Aviões?\nApenas letra e número exemplo, A12; T1")
        posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                         " a partir da coordenada dada"))

        # Validacao da coordenada do Cruzador
        while len(posicaoNavio[0]) != 1 or posicaoNavio[0] > "T" or posicaoNavio[1] >= 18 or \
                posicaoNavio[1] < 1 \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] != "' " \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1]] != "' " \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + 1] != "' " \
                or mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + 2] != "' ":
            print("coordenada invalida, ou navio já existente na coordenada")
            print("Onde deseja inserir o Porta-Aviões?\nApenas letra e número exemplo, A12; T1")
            posicaoNavio = array_coordenada(input_caixa_alta("Será inserido automaticamente o barco inteiro" +
                                                             " a partir da coordenada dada"))

        # Inserir "P " na casa determinada e na proxima a direita
        for prox in range(-1, 3):
            mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] + prox] = "P "
        # aumentar o contador de Porta-Aviões
        nPortaAvioes += 1
        # imprimir o mapa com o novo barquinho a partir de funcao imprimir_mapa
        imprimir_mapa(mapaP1)
    elif escolhaNavio == "P" and nPortaAvioes >= 3:
        print("Voce ja posicionou todos os 3 Porta-Aviões")
    else:
        print("Escolha inválida")

#Parte para Player 2
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTodos os navios posicionados, hora do Jogador 2 retornar ao teclado")
time.sleep(4)

mapaP2 = matrizDinamica
imprimir_mapa(mapaP2)
imprimir_mapa(mapaP1)

#Selecionar a dificuldade. Interfere na quantidade de tentativas apenas
dificuldade = input_caixa_alta("Selecione o nivel de dificuldade: D para difícil; M para médio; F para fácil")
#Validacao da dificuldade
while dificuldade != "D" and dificuldade != "M" and dificuldade != "F":
    print("Opcão invalida")
    dificuldade = input_caixa_alta("Selecione o nivel de dificuldade: D para dificil; M para medio; F para fácil")

if dificuldade == "D":
    dificuldade = 100
    print("Parece que temos alguem corajoso aqui\nVocê terá 100 chances para derrubar todos os 12 navios\nBoa Sorte.")
elif dificuldade == "M":
    dificuldade = 300
    print("Você terá 300 chances para derrubar os 12 navios expalhados por 400 casas\nBoa Sorte.")
elif dificuldade == "F":
    dificuldade = 1000
    print("Está com medo de perder?!\nVoce terá mais chances do que lugares para procurar\nBom Jogo")


while nFragatas > 0 or nCruzadores > 0 or nPortaAvioes > 0 or dificuldade > 0:
    posicaoNavio = array_coordenada(input_caixa_alta("Onde vc acha que estão os navios inimigos?\n" +
                                    "Apenas letra e número exemplo, A12; T1"))
    print(posicaoNavio)
    imprimir_mapa(mapaP2)
    imprimir_mapa(mapaP1)
    while len(posicaoNavio[0]) != 1 or posicaoNavio[0] > "T" or posicaoNavio[1] > 20 or \
                posicaoNavio[1] <= 0 or mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] != "' ":
        print("Opcão invalida ou ja selecionada anteriormente")
        posicaoNavio = array_coordenada(input_caixa_alta("Onde vc acha que estão os navios inimigos?\n" +
                                        "Apenas letra e número exemplo, A12; T1"))

    #Navio atingido
    if mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] != "' " and dificuldade > 0:
        print("Você acertou um navio")
        (mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1]) = (mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1])
        #verificar qual tipo de navio foi atingido
        if mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] == "F ":
            fAtingidas += 1
        elif mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] == "C ":
            cAtingidos += 1
        elif mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] == "P ":
            pAtingidos += 1
        imprimir_mapa(mapaP2)

        dificuldade = dificuldade - 1

    #Nenhum navio atingido
    elif mapaP1[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] == "' " and dificuldade > 0:
        mapaP2[ord(posicaoNavio[0]) - 65][posicaoNavio[1] - 1] = "A "
        imprimir_mapa(mapaP2)
        print("Voce acertou a agua :(")

        dificuldade = dificuldade - 1

    #checkpoint
    else:
        print("Se vc está lendo isso deu ruim no codigo linha 240")

    #descontar navios naufragados e acrescentar pontos
    if fAtingidas == 2:
        nFragatas = nFragatas - 1
        fAtingidas = 0
        pontos += 10
    if cAtingidos == 3:
        nCruzadores = nCruzadores - 1
        cAtingidos = 0
        pontos += 20
    if pAtingidos == 4:
        nPortaAvioes = nPortaAvioes - 1
        pAtingidos = 0
        pontos += 30

#Finalizar o Jogo
if dificuldade <= 0 and (nFragatas > 0 or nCruzadores > 0 or nPortaAvioes > 0):
    print("Jogador 2 não consegiu destruir todos os navios\nJogador 1 vence o Jogo")
    print("Pontuacão Jogador 2: " + pontos)
elif dificuldade > 0 and nFragatas <= 0 and nCruzadores <= 0 and nPortaAvioes <= 0:
    print("Jogador 2 afundou todos a frota do Jogador 1\nJogador 2 vence o Jogo")
    print("Pontuacão Jogador 2: " + pontos)