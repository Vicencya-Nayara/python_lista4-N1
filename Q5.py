#Implemente uma fila circular utilizando um vetor e as operações básicas.

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaCircular:
    def __init__(self, tamanho=None):
        self.inicio = None
        self.fim = None
        self.tamanho = tamanho if tamanho is not None else float('inf')
        self.contagem = 0

    def enfileirar(self, valor):
        if self.esta_cheia():
            raise IndexError('A fila está cheia')
        novo_item = Item(valor)
        if self.esta_vazia():
            self.inicio = novo_item
            self.fim = novo_item
            novo_item.proximo = self.inicio
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item
            self.fim.proximo = self.inicio
        self.contagem += 1
    
    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError('A fila está vazia')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        self.contagem -= 1
        if self.inicio is None:
            self.fim = None
        return valor
    
    def esta_vazia(self):
        return self.inicio is None
    
    def esta_cheia(self):
        return self.contagem >= self.tamanho 
    
    def tamanho(self):
        return self.contagem
    
    def elemento_final(self):
        if self.esta_vazia():
            raise IndexError('A fila está vazia')
        return self.fim.valor
    
    def proximo_elemento(self):
        if self.esta_vazia():
            raise IndexError('A fila está vazia')
        return self.inicio.valor
    
    def __str__(self):
        s = ""
        aux = self.inicio
        for i in range(self.contagem):
            s += str(aux.valor) + " "
            aux = aux.proximo
        return s

filacircular = FilaCircular()
print('Inserindo elementos:')
x = int(input('Digite quantos itens você quer adicionar: '))
for i in range(x):
    filacircular.enfileirar(input(f'Digite o {i + 1}° item: '))

print(f'\nMostrando a fila: {filacircular}')
print(f'\nRemovendo elemento: {filacircular.desenfileirar()}')
