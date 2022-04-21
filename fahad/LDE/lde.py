# Lista Duplamente Encadeada com uso de Sentinelas

class Dnodo:
    def __init__(self, dado = None):
        self.dado = dado
        self.anterior = None
        self.proximo = None

    def __str__(self):
        return str(self.dado)

class LDE:
    def __init__(self):
        self.header = Dnodo()   # <<< Sentinela Cabeça
        self.trailer = Dnodo()  # <<< Sentinela Cauda
        self.tam = 0            # qtde de itens na lista

    def is_empty(self):
        if self.header.proximo is None and self.trailer.anterior is None:
            return True
        return False

    def __inserir(self, novo):
        self.header.proximo = novo    # header -> novo
        novo.anterior = self.header   # header <- novo
        novo.proximo = self.trailer   # novo -> trailer
        self.trailer.anterior = novo  # novo <- trailer
      
    def inserirInicio(self, novo):
        self.tam += 1
        if self.is_empty():
            self.__inserir(novo)
        else:
           pass

    def inserirFim(self, novo):
        self.tam += 1
        if self.is_empty():
            self.__inserir(novo)
        else:
            pass
    
    def removerInicio(self):
        if self.is_empty():
            print('Lista Vazia!')
            return
        else:
            # lista possui + de 1 item            
            removido = self.header.proximo
            self.header.proximo = removido.proximo
            removido.proximo.anterior = self.header
            removido.anterior = None
            removido.proximo = None
            
        self.tam -= 1            
        return removido
        
    def removerFim(self):
        if self.is_empty():
            print('Lista Vazia!')
            return
        
        else:
            # refazer os apontamentos
            removido = self.trailer.anterior
            self.trailer.anterior = removido.anterior
            removido.anterior.proximo = self.trailer
            removido.anterior = None
            removido.proximo = None
            pass

        self.tam -= 1
        return removido

    def imprimir(self, reverso=False):
        if self.is_empty():
            print('Lista Vazia')
            return

        if not reverso:
            item = self.header.proximo # devolve o 1o da lista
            while (item.proximo is not None):
                print(item)
                item = item.proximo
        else:
            item = self.trailer.anterior # devolve o ultimo da lista
            while (item.anterior is not None):
                print(item)
                item = item.anterior
    
    def buscar(self, alvo):# retorna a 1a ocorrencia
        if self.is_empty():
            print('Lista Vazia')
            return
        else:
            item = self.header.proximo
            while (item.dado != alvo):
                if (item.proximo is None):
                    return None
                item = item.proximo
            return item
        pass

    def get(self, indice):
        if indice < 0 or indice >= self.tam:
            contador = 0
            item = self.header.proximo
            while item.proximo is not None:
                if contador == indice:
                    return item.dado
                contador += 1
        else:
            raise Exception('Indice fora do intervalo')
        pass

    def removerAntes(self, alvo):
        # header <-> [] <-> [] <-> trailer
        
        nodo_atual = self.buscar(alvo)
        nodo_anterior = nodo_atual.anterior
        
        if (nodo_anterior != self.header):            
            aux = nodo_anterior.anterior
            aux.proximo = nodo_atual
            nodo_atual.anterior = aux
            
            nodo_anterior.anterior = None
            nodo_anterior.proximo = None
            
        self.tam -= 1
        
    def removerApos(self, alvo):
        pass    

    def substituir(self, alvo, valor):
        pass

    def buscarTodos(self, alvo): # retorna uma list com resultados
        lista_todos = []
        ##
        ## sua logica aqui
        ##
        return lista_todos

    def primeiro(self):
        if self.is_empty():
            print('Lista Vazia')
            return
        else:
            return self.header.proximo

    def ultimo(self):
        pass

    def __len__(self):
        return self.tam

## TESTES ##

lista = LDE()
lista.inserirInicio(Dnodo('abc'))
lista.inserirInicio(Dnodo('001'))
lista.inserirInicio(Dnodo('xyz'))
lista.removerInicio()
lista.removerInicio()
lista.removerInicio()
lista.removerInicio()
lista.imprimir()