#Prof, não obtive sucesso em utilizar a class que usamos na aula, não lembro se era necessáriopor isso acabei fazendo de outra forma

print("Bem Vindo ao Validador de Expressões")

expressao = input("Digite a Expressao: ")
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] == "(":
        pilha.append("(")
    if expressao[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x = x + 1
if len(pilha) == 0:
    print("Valida")
else:
    print("Invalida")


