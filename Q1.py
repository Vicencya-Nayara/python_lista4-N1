#Implemente uma fila simples e as operações básicas: inserir, remover e mostrar o elemento da frente.

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Fila:
    def __init__(self):
        self.comeco = None
        self.final = None
        self.tamanho = 0

    def is_empty(self):
        return self.comeco is None
    
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.comeco = novo_item
            self.final = self.comeco
        else:
            self.final.prox = novo_item
            self.final = novo_item
        self.tamanho += 1

    def desinfileirar(self):
        if self.is_empty():
            raise IndexError('A lista está vazia')
        valor = self.comeco.valor
        self.comeco = self.comeco.prox
        if self.comeco is None:
            self.final = None
        
        self.tamanho -= 1
        return valor
    
    def get_tamanho(self):
        return self.tamanho
    
def filSimples():
    fila = Fila()

    for i in range(5):
        fila.enfileirar(i)

    while not fila.is_empty():
        proximo = None
        if fila.comeco.prox is not None:
            proximo = fila.comeco.prox.valor
        print(f'Removendo: {fila.desinfileirar()} Proximo: {proximo}')
    
    print('Valores removidos')

filSimples()



