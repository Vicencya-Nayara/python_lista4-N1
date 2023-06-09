#Escreva um programa que leia uma lista de nomes e crie uma lista encadeada dupla com esses nomes em ordem alfabética.

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def is_vazia(self):
        return self.inicio is None
    
    def tamanho(self):
        return self.tamanho

    def inserir_inicio(self, elemento):
        novo_item = Item(elemento)
        if self.is_vazia():
            self.inicio = novo_item
        else:
            novo_item.prox = self.inicio
            self.inicio.ant = novo_item
            self.inicio = novo_item
        self.tamanho += 1
    
    def inserir_fim(self, elemento):
        novo_item = Item(elemento)
        if self.is_vazia():
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo_item
            novo_item.ant = atual
        self.tamanho += 1

    def inserir_ordenado(self, elemento):
        novo_item = Item(elemento)
        if self.is_vazia() or elemento < self.inicio.valor:
            self.inserir_inicio(elemento)
            return
        atual = self.inicio
        while atual.prox is not None and atual.prox.valor < elemento:
            atual = atual.prox
        novo_item.prox = atual.prox
        novo_item.ant = atual
        if atual.prox is not None:
            atual.prox.ant = novo_item
        atual.prox = novo_item
        self.tamanho += 1

    def remover_inicio(self):
        if self.is_vazia():
            raise IndexError('A lista está vazia')
        valor = self.inicio.valor
        self.inicio = self.inicio.prox
        if self.inicio is not None:
            self.inicio.ant = None
        self.tamanho -= 1
        return valor

    def remover_fim(self):
        if self.is_vazia():
            raise IndexError('A lista está vazia')
        if self.inicio.prox is None:
            valor = self.inicio.valor
            self.inicio = None
            self.tamanho -= 1
            return valor
        atual = self.inicio
        while atual.prox is not None:
            atual = atual.prox
        valor = atual.valor
        atual.ant.prox = None
        self.tamanho -= 1
        return valor

    def buscar(self, item):
        if self.is_vazia():
            raise IndexError('A lista está vazia')
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return True
            aux = aux.prox
        return False

    def exibir_lista(self):
        if self.is_vazia():
            print('A lista está vazia!')
        else:
            aux = self.inicio
            while aux is not None:
                print(aux.valor, end=" ")
                aux = aux.prox
            print()


nomes = input('Digite uma lista de nomes separados por espaço: ').split()
lista = ListaEncadeadaDupla()

for nome in nomes:
    lista.inserir_ordenado(nome)

print('Lista Encadeada Dupla em ordem alfabética:')
lista.exibir_lista()
