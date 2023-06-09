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


num_elementos = int(input('Digite a quantidade de elementos que você quer inserir: '))
lista = ListaEncadeada()

for i in range(num_elementos):
    valor1 = input('Digite um valor para inserir no início da lista: ')
    lista.inserir_inicio(valor1)
    valor2 = input('Digite um valor para inserir no final da lista: ')
    lista.inserir_fim(valor2)
    print(f'\nMostrando a lista: ', end="")
    lista.exibir_lista()

print('Removendo do início.')
lista.remover_inicio()

print('Removendo do final.')
lista.remover_fim()

print('Mostrando a Lista Final: ', end="")
lista.exibir_lista()
