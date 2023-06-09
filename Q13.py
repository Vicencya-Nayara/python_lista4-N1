#Implemente uma lista encadeada circular e as operações básicas: inserir no início, inserir no final, 
#remover do início, remover do final e exibir a lista.

class Item:
    def __init__(self, value):
        self.value = value
        self.prox = None

class ListaEncadeadaCircular:
    def __init__(self, tamanho=None):
        self.inicio = None
        self.size = tamanho if tamanho is not None else float('inf')
        self.count = 0

    def is_empty(self):
        return self.inicio is None
    
    def is_full(self):
        return self.count >= self.size
    
    def tamanho(self):
        return self.count
    
    def inserir_fin(self, elemento):
        if self.is_full():
            raise Exception('A lista está cheia!')
        new_item = Item(elemento)
        if self.is_empty():
            self.inicio = new_item
            new_item.prox = self.inicio
        else:
            aux = self.inicio
            while aux.prox != self.inicio:
                aux = aux.prox
            aux.prox = new_item
            new_item.prox = self.inicio
        self.count += 1

    def inserir_ini(self, elemento):
        if self.is_full():
            raise Exception('A lista está cheia!')
        new_item = Item(elemento)
        if self.is_empty():
            self.inicio = new_item
            new_item.prox = self.inicio
        else:
            aux = self.inicio
            while aux.prox != self.inicio:
                aux = aux.prox
            aux.prox = new_item
            new_item.prox = self.inicio
            self.inicio = new_item
        self.count += 1

    def remover_ini(self):
        if self.is_empty():
            raise IndexError('A lista está vazia')
        valor = self.inicio.value
        if self.inicio.prox == self.inicio:
            self.inicio = None
        else:
            aux = self.inicio
            while aux.prox != self.inicio:
                aux = aux.prox
            aux.prox = self.inicio.prox
            self.inicio = self.inicio.prox
        self.count -= 1
        return valor
    
    def remover_fin(self):
        if self.is_empty():
            raise IndexError('A lista está vazia')
        if self.inicio.prox == self.inicio:
            valor = self.inicio.value
            self.inicio = None
            self.count -= 1
            return valor
        p = self.inicio
        a = None
        while p.prox != self.inicio:
            a = p
            p = p.prox
        a.prox = self.inicio
        valor = p.value
        self.count -= 1
        return valor
    
    def buscar(self, item):
        if self.inicio is None:
            raise IndexError('A lista está vazia')
        aux = self.inicio
        while True:
            if aux.value == item:
                return True
            aux = aux.prox
            if aux == self.inicio:
                break
        return False

    def prim_item(self):
        return self.inicio.value
    
    def ult_item(self):
        aux = self.inicio
        while aux.prox != self.inicio:
            aux = aux.prox
        return aux.value

    def __str__(self):
        if self.is_empty():
            return 'A lista está vazia.'
        s = ""
        aux = self.inicio
        while True:
            s += str(aux.value) + " "
            aux = aux.prox
            if aux == self.inicio:
                break
        return s


lista = ListaEncadeadaCircular()

num_itens = int(input('Digite a quantidade de itens que você quer inserir: '))

for i in range(num_itens):
    nome_inicial = input('Digite um nome para inserir no início: ')
    lista.inserir_ini(nome_inicial)
    nome_final = input('Digite um nome para inserir no final: ')
    lista.inserir_fin(nome_final)
    print(f'\nMostrando a lista: {lista}')

print('Removendo no início.') 
print(lista.remover_ini())

print('Removendo no final.') 
print(lista.remover_fin())

print(f'Mostrando a lista final: {lista}')

