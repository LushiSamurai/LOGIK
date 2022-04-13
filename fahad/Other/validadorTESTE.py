#Prof, fiz este validador instanciando a pilha com a class que utilizamos na aula
#Ele funciona, porém quando a expressão não é valida ele retorna Invalida e Valida junto
from PILHA import *

print("Bem Vindo ao Validador de Expressões")

if __name__ == "__main__":
    p1 = Pilha()
    expressao = (input('Escreva a Expressão: '))
    exprAbrir = ['{','[','(']
    exprFechar= ['}',']',')']
    for i in range(len(expressao)):
        if expressao[i] in exprAbrir:
            p1.push(expressao[i])
        elif expressao[i] in exprFechar:
            if len(p1) == 0:
                print('Inválida')
                break
            elif p1.peek() == '{' and expressao[i] == '}':
                p1.pop()
            elif p1.peek() == '[' and expressao[i] == ']':
                p1.pop()
            elif p1.peek() == '(' and expressao[i] == ')':
                p1.pop()
            else:
                print('Inválida')
                break
        else:
            continue
    if len(p1) == 0:
        print('Válida')