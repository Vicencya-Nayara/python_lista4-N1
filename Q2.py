#Crie um programa que exibe ao usuário um menu com as seguintes opções: adicionar número na fila; remover número da fila; 
#tamanho da fila; mostrar fila. Todas as opções devem funcionar conforme a ação que ela descreve.

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.tail = novo_item
            self.head = novo_item
        else:
            self.tail.proximo = novo_item
            self.tail = novo_item
        self.tamanho += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')
        valor = self.head.valor
        self.head = self.head.proximo
        if self.head is None:
            self.tail = None
        self.tamanho -= 1
        return valor

def menu(opcao, fila):
    if opcao == 1:
        valor = int(input('Digite o número a ser inserido: '))
        fila.enqueue(valor)
    elif opcao == 2:
        try:
            remover = fila.dequeue()
            print('Valor removido:', remover)
        except IndexError as e:
            print(e)
    elif opcao == 3:
        tamanho = fila.tamanho
        print('O tamanho da fila é:', tamanho)
    elif opcao == 4:
        if fila.is_empty():
            print('A fila está vazia.')
        else:
            print('Números na fila:')
            mostrarItem = fila.head
            while mostrarItem is not None:
                print(mostrarItem.valor)
                mostrarItem = mostrarItem.proximo
    else:
        print('Opção não existente!')

fila = Queue()

while True:
    print('Escolha uma função digitando o número referente')
    print('1 - Inserir')
    print('2 - Remover')
    print('3 - Tamanho')
    print('4 - Mostrar')
    print('5 - Sair')
   
    opcao = int(input('Digite um número referente a uma função: '))
   
    if opcao == 5:
        print('Você saiu!')
        break
   
    menu(opcao, fila)
