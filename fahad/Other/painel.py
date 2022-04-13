from fila import Fila

fila = Fila()

senhas = []

contador = 0


def verificaOpcao():
    global contador

    if opcaoDesejada == 1:
        print(f"Sua senha para espera é {contador}")
        fila.enqueue(contador)
        contador += 1
        menu()

    elif opcaoDesejada == 2:
        senhas.append(fila._vet[0])
        print(F"A senha no momento {fila._vet[0]}")
        fila.dequeue()
        menu()

    elif opcaoDesejada == 3:
        print(f"As senhas já chamadas: {senhas}")
        menu()

    else:
        print("Essa opção não existe. Por favor, tente novamente.")
        menu()


def menu():
    global opcaoDesejada
    opcaoDesejada = int(input(
        "Digite 1 se você quer obter uma nova senha, 2 se você quer chamar a próxima senha e 3 se você quer mostras as senhas chamadas: "))
    verificaOpcao()


menu()