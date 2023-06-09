#Implemente uma lista encadeada dupla e as operações básicas: inserir no início, inserir no final, 
#remover do início, remover do final e exibir a lista.

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

lista = ListaEncadeadaDupla()
num_itens = int(input('Digite a quantidade de itens que você quer inserir: '))

for i in range(num_itens):
    print('Inserindo no início.')
    lista.inserir_inicio(input('Digite algo: '))
    print('Inserindo no final.')
    lista.inserir_fim(input('Digite algo: '))
    print('\nMostrando a lista: ')
    lista.exibir_lista()

print(f'Removendo no início: {lista.remover_inicio()}') 

print('Removendo no final:')
valor_removido = lista.remover_fim()
if valor_removido is not None:
    print(valor_removido)

print('Lista final: ')
lista.exibir_lista()
