import random

def adivinhador_maquina():
    print("Vou escolher um número entre 1 e 100, e você tentará adivinhá-lo.")

    numero_a_adivinhar = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Faça a sua tentativa: "))
        tentativas += 1

        if tentativa < numero_a_adivinhar:
            print("Tente um número maior.")
        elif tentativa > numero_a_adivinhar:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_a_adivinhar} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinhador_maquina()
