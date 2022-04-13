#include <iostream> std

from random import random
from LSE import * 
from fila import *
from catto import kitty

racasGatos = ["Siamês", "Sphynx", "Russo", ]
coresGatos = ["Amarelo", "Azul", "Branco", "Cinza", "Marrom", "Preto"]


def menu():
    print ("1 - Listar as Raças disponiveis",
    "\n2 - Listar as Cores disponiveis",
    "\n3 - Sair"
    )
    global opt
    opt = int(input("Escolha uma opção: "))
    Opcao()
    
def Opcao():
    global gato
    
    if opt == 1:
        print(f"As raças disponiveis são: {racasGatos}")
        print(input(f"Deseja adicionar uma raça? (S/N): "))
        if input == "S" or "s":
            print(input("Digite a raça: "))
            racasGatos.append(input)
            print(f"As raças disponiveis são: {racasGatos}")
        elif input == "N" or "n":
            print("Ok, vamos continuar")
            menu()
        
    elif opt == 2:
        print(f"As cores disponiveis são: {coresGatos}")
        print(input("Deseja adicionar uma cor? (S/N): "))
        if input == "S" or "s":
            print(input("Digite a cor: "))
            coresGatos.append(input)
            print(f"As cores disponiveis são: {coresGatos}")
        elif input == "N" or "n":
            print("Ok, vamos continuar")
            menu()

    elif opt == 3:
        print("Saindo...")
        exit()    

    elif opt == 0:
        kitty()
        menu()
        
    else:
        print("Opção inválida")
        menu()
    
menu()

