#Implemente uma lista encadeada simples e as operações básicas: inserir no início, 
#inserir no final, remover do início, remover do final e exibir a lista.


class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None

    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.inicio
        self.inicio = novo_item
        self.tamanho += 1

    def inserir_fim(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item
        self.tamanho += 1

    def remover_inicio(self):
        if self.vazia():
            print("A lista está vazia!")
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def remover_fim(self):
        if self.vazia():
            print("A lista está vazia!")
        elif self.inicio.proximo is None:
            self.inicio = None
            self.tamanho -= 1
        else:
            atual = self.inicio
            anterior = None
            while atual.proximo is not None:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None
            self.tamanho -= 1

    def exibir_lista(self):
        if self.vazia():
            print("A lista está vazia!")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual.valor, end=" ")
                atual = atual.proximo
            print()


lista = ListaEncadeada()

lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_fim(30)
lista.inserir_fim(40)

lista.exibir_lista()  

lista.remover_inicio()
lista.remover_fim()

lista.exibir_lista()  
