from PILHA import *

print("Conversor de Número Decimal para Binário")

if __name__ == "__main__":
    pilha = Pilha()
    numero = int(input("Digite um numero: "))
    while numero > 0:
        resto = numero % 2
        pilha.push(resto)
        numero = numero // 2
    while len(pilha) > 0:
        print(pilha.pop(), end="")
    print("")