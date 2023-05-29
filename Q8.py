#Escreva um programa que leia uma lista de números inteiros e crie uma lista encadeada simples com esses números em ordem inversa.

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

    def exibir_lista(self):
        if self.vazia():
            print("A lista está vazia!")
        else:
            atual = self.inicio
            while atual is not None:
                print(atual.valor, end=" ")
                atual = atual.proximo
            print()

def criar_lista_inversa(numeros):
    lista = ListaEncadeada()
    for numero in numeros:
        lista.inserir_inicio(numero)
    return lista

numeros = input("Digite os números inteiros separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

lista_inversa = criar_lista_inversa(numeros)

print("Lista encadeada inversa:")
lista_inversa.exibir_lista()
