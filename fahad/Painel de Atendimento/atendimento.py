#include <iostream> std
from catto import kitty
from fila import *

fila = fila()
keyw = []
contador = 0


def menu():
    print ("1 - Gerar Senha",
    "\n2 - Chamar a proxima senha",
    "\n3 - Ultima Senha chamada",
    "\n4 - Sair"
    )
    global opt
    opt = int(input())
    Opcao()
  

def Opcao():
    global contador

    if opt == 1:
        print(f"Sua senha é: {contador}")
        fila.enqueue(contador)
        contador += 1
        menu()

    elif opt == 2:
        keyw.append(fila._vet[0])
        print(f"!!ATENÇÃO!! \n SENHA: {fila._vet[0]}")
        fila.dequeue()
        menu()

    elif opt == 3:
        print(f"Ultimas senhas chamadas: {keyw}")
        if fila.is_empty():
            print("Não há senhas chamadas")
        menu()

    elif opt == 4:
        print("Saindo...")
        exit()    

    elif opt == 0:
        kitty()
        menu()
        
    else:
        print("Opção inválida")
        menu()
    
menu()



