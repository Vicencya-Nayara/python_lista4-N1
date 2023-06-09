#Crie um jogo de simulação de roleta utilizando uma lista encadeada circular. 
#Cada elemento da lista deve representar um número da roleta, e o jogador deve apostar em um número. 
#Ao girar a roleta, o programa deve percorrer a lista até encontrar o número sorteado 
#e indicar se o jogador ganhou ou perdeu.

import random

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.inicio = None
        self.quantidade = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir_ordenado(self, elemento):
        novo_item = Item(elemento)
        if self.esta_vazia():
            novo_item.prox = novo_item
            self.inicio = novo_item
        elif elemento <= self.inicio.valor:
            novo_item.prox = self.inicio
            ultimo = self.inicio
            while ultimo.prox != self.inicio:
                ultimo = ultimo.prox
            ultimo.prox = novo_item
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.prox != self.inicio and atual.prox.valor < elemento:
                atual = atual.prox
            novo_item.prox = atual.prox
            atual.prox = novo_item
        self.quantidade += 1

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

# Função para simular o jogo da roleta
def jogo_roleta(lista):
    if lista.esta_vazia():
        print("A roleta está vazia. O jogo não pode ser iniciado.")
        return

    numero_sorteado = random.choice(range(1, lista.quantidade+1))
    print("Número sorteado:", numero_sorteado)

    aux = lista.inicio
    while True:
        if aux.valor == numero_sorteado:
            print("Parabéns! Você ganhou.")
            return
        aux = aux.prox
        if aux == lista.inicio:
            break

    print("Que pena! Você perdeu.")

# Programa principal
lista = ListaEncadeadaCircular()
numeros = input("Digite uma lista de números inteiros separados por espaço: ")
numeros = numeros.split()
for numero in numeros:
    lista.inserir_ordenado(int(numero))

print("Roleta criada:")
print(lista)

jogo_roleta(lista)


