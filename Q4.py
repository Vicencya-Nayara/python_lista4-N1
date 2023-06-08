#Escreva um programa que leia uma frase do usuário e verifique se ela é um palíndromo 
#(ou seja, pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda). 
#Utilize uma fila para armazenar os caracteres da frase.

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

def verificar_palindromo(frase):
    fila = Fila()

    for char in frase:
        fila.enfileirar(char)

    tamanho = fila.tamanho
    for i in range(tamanho // 2):
        if fila.desinfileirar() != frase[tamanho - i - 1]:
            return False

    return True

frase = input("Digite uma frase: ")

if verificar_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")













        

