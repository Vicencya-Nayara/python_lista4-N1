#Escreva um programa que leia uma lista de números inteiros e crie uma lista encadeada circular com esses 
#números em ordem crescente. Sua classe lista deve conter métodos/funções para mostrar o primeiro e ultimo elemento da lista. 

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.inicio = None
        self.count = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir_ordenado(self, elemento):
        novo_item = Item(elemento)
        if self.esta_vazia() or elemento <= self.inicio.valor:
            novo_item.prox = self.inicio
            self.inicio = novo_item
            if self.inicio.prox is None:
                self.inicio.prox = self.inicio
            else:
                ultimo = self.inicio
                while ultimo.prox != self.inicio:
                    ultimo = ultimo.prox
                ultimo.prox = self.inicio
        else:
            atual = self.inicio
            while atual.prox != self.inicio and atual.prox.valor < elemento:
                atual = atual.prox
            novo_item.prox = atual.prox
            atual.prox = novo_item
        self.count += 1

    def primeiro_elemento(self):
        if self.esta_vazia():
            raise IndexError('A lista está vazia')
        return self.inicio.valor

    def ultimo_elemento(self):
        if self.esta_vazia():
            raise IndexError('A lista está vazia')
        aux = self.inicio
        while aux.prox != self.inicio:
            aux = aux.prox
        return aux.valor

    def __str__(self):
        if self.esta_vazia():
            return 'A lista está vazia.'
        s = ""
        aux = self.inicio
        while True:
            s += str(aux.valor) + " "
            aux = aux.prox
            if aux == self.inicio:
                break
        return s

lista = ListaEncadeadaCircular()
numeros = input("Digite uma lista de números inteiros separados por espaço: ")
numeros = numeros.split()
for numero in numeros:
    lista.inserir_ordenado(int(numero))
print("Lista encadeada circular criada:")
print(lista)
if not lista.esta_vazia():
    try:
        print("Primeiro elemento da lista:", lista.primeiro_elemento())
        print("Último elemento da lista:", lista.ultimo_elemento())
    except IndexError as e:
        print(e)
