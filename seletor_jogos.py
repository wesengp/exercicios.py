import time
import advinhacao
import forca

print("Qual Jogo vamos jogar Hoje")
print("(1) ---- Forca\n(2) ---- Adivinhação")
jogar = int(input("Escolha seu o Jogo: "))

if (jogar == 1):
    print("Entrando no jogo da Forca")
    print("Carregando...")
    time.sleep(2)
    forca.jogar()
elif(jogar == 2):
    print("Entrando no jogo de Advinhação")
    print("Carregando...")
    time.sleep(2)
    advinhacao.jogar()

