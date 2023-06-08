#Escreva um programa que leia uma sequência de números inteiros e insira-os em uma fila até que um número negativo seja digitado. 
#Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.

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
            raise IndexError('A fila está vazia')
        valor = self.comeco.valor
        self.comeco = self.comeco.prox
        if self.comeco is None:
            self.final = None

        self.tamanho -= 1
        return valor

fila = Fila()

while True:
    numero = int(input("Digite um número inteiro ou um número negativo para parar: "))
    if numero < 0:
        break
    fila.enfileirar(numero)

print("Elementos da fila:")
while not fila.is_empty():
    elemento = fila.desinfileirar()
    print(elemento)
