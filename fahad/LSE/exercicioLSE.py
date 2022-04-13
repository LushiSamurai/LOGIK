#include <iostream> std
#[LSE]

#- Método buscar() [contains]
#- Método limpar()

#- Implementar um método get() --- o usuário passa uma posição e retorna o Nodo encontrado
#- Implementar método to_list() --- Devolve o conteúdo dos nodos em uma List do Python

#-> Criar uma implementação de pilha baseada na LSE

#** Pode ser em DUPLAS, mas cada aluno realiza sua entrega **

#PilhaEncadeada   
#   push
#   pop
#   peek
#   __len_

from LSE import *
from catto import kitty

fila = LSE()
keyw = []
contador = 0


def menu():
    print ("1 - Gerar Senha",
    "\n2 - Chamar a proxima senha",
    "\n3 - Historico de senhas chamadas",
    "\n4 - Sair"
    )
    global opt
    opt = int(input("Escolha uma opção: "))
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







