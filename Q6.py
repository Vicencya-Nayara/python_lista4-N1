#Considere um supermercado que atende a inúmeros clientes. Cada cliente possui um número de identificação 
#único e chega ao supermercado em momentos distintos. Implemente um sistema que receba a chegada de clientes 
#e mantenha uma fila para o atendimento. A cada hora*, o sistema deve atender o próximo cliente da 
#fila e imprimir o número de identificação desse cliente.

import time
import random

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
fila_h = Fila()

num_client = int(input('Digite a quantidade de clientes que estarão na fila do mercado: '))

def adicionar_clientes():
    for i in range(num_client):
        x = random.randint(1, 100)
        fila.enfileirar(x)
        fila_h.enfileirar(time.strftime("%H:%M:%S"))
        time.sleep(1)

def atender_clientes():
    while not fila.is_empty():
        h_cliente = fila_h.desinfileirar()
        cod_cliente = fila.desinfileirar()
        print(f'No horário {h_cliente}, o cliente com o código {cod_cliente} chegou.')
        print(f'No horário {time.strftime("%H:%M:%S")}, o cliente do código {cod_cliente} foi atendido.\n')
        time.sleep(5)

adicionar_clientes()
print(f'\nFila de clientes por seus códigos: {fila}\n')
atender_clientes()
