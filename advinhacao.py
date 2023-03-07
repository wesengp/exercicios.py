import random
import time
def jogar():
    print("***********************************************************")
    print("Bem vindo ao Jogo de Advinhação")
    print("***********************************************************")
    numeroCerto = random.randint(1, 10)
    total_de_tentativas = 0
    print("Qual nível de dificuldade: ")
    print("(1) ----- Fácil \n(2) ----- Médio \n(3)----- Difícil")

    nivel = int(input("Informe a dificuldade:"))
    print("***********************************************************")
    print("Estou pensando em um numero entre 1 e 10")
    print("***********************************************************")


    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1 ):
        print()
        print("Processando.....")
        print()
        time.sleep(1)
        print("tentativa {} de {} ".format(rodada,total_de_tentativas))
        print()
        chute = int(input("Digite um número: "))
        print("Voce digitou",chute)

        certo = chute == numeroCerto
        maior = chute > numeroCerto
        menor = chute < numeroCerto

        if (chute < 1 ):
            print("Preste atenção cavalo entre 1 e 10")
            continue
        if (chute > 10):
            print("Acho que você deve ter problemas entre 1 e 10 MEU DEUS!!!")
            continue

        if (certo):
            print("UAU NÚMERO CORRETO VOCÊ É DEMAIS!!!!")
            print("*************************************")
            print("Você Venceu")
            print("*************************************")

            break

        else:
            if (maior):
                print("O número digitado é maior que o numero certo")
                print("Você perdeu..")
            elif(menor):
                print("O número digitado é menor que o numero certo ")
                print("Você perdeu..")
    print()
    print("Fim do Jogo")
