class fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)
        return None

    def front(self): # 1o da fila sem remover
        if not self.is_empty():
            return self._vet[0]
        return None
                
    def is_empty(self): # fila vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # string
        return str(self._vet)
