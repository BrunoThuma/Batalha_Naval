from random import randint

def uppercase_input(msg):
    print(msg)
    text = str(input())
    text = text.upper()
    return text

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def find_number(givenString):
    newList = list(givenString)
    numbersFound = 0
    numbersStr = '0'
    for cont in range (len(newList)):
        if hasNumbers(newList[cont]) and numbersFound == 0:
            numbersStr = newList[cont]
            numbersFound += 1
        elif hasNumbers(newList[cont]) and numbersFound == 1:
            numbersStr += newList[cont]
    return int(numbersStr)

def find_letter(givenString):
    newList = list(givenString)
    lettersFound = 0
    lettersStr = '0'
    for cont in range(len(newList)):
        if not hasNumbers(newList[cont]) and lettersFound == 0:
            lettersStr = newList[cont]
            lettersFound += 1
        elif not hasNumbers(newList[cont]) and lettersFound == 1:
            lettersStr += newList[cont]
    return str(lettersStr)

def auto_ship():

    return

def print_map():
    print(" ".join(identificationLine))
    print(" ".join(line1))
    print(" ".join(line2))
    print(" ".join(line3))
    print(" ".join(line4))
    print(" ".join(line5))
    print(" ".join(line6))
    print(" ".join(line7))
    print(" ".join(line8))
    print(" ".join(line9))
    print(" ".join(line10))
    print(" ".join(line11))
    print(" ".join(line12))
    print(" ".join(line13))
    print(" ".join(line14))
    print(" ".join(line15))
    print(" ".join(line16))
    print(" ".join(line17))
    print(" ".join(line18))
    print(" ".join(line19))
    print(" ".join(line20))

portaAvioes1 = []
portaAvioes2 = []
portaAvioes3 = []
cruzador1 = []
cruzador2 = []
cruzador3 = []
cruzador4 = []
fragata1 = []
fragata2 = []
fragata3 = []
fragata4 = []
fragata5 = []

identificationLine = ["  ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","11","12","13","14","15","16",\
                      "17","18","19","20"]
line1 = ["A ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line2 = ["B ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line3 = ["C ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line4 = ["D ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line5 = ["E ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line6 = ["F ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line7 = ["G ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line8 = ["H ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line9 = ["I ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line10 = ["J ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line11 = ["K ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line12 = ["L ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line13 = ["M ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line14 = ["N ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line15 = ["O ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line16 = ["P ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line17 = ["Q ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line18 = ["R ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line19 = ["S ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]
line20 = ["T ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "," "," "," "," "," "]

print_map()