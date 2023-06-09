#Crie uma agenda telefônica utilizando uma lista encadeada dupla. Cada entrada na agenda deve conter o nome
#e o número de telefone de uma pessoa. Implemente as operações de inserir, remover e buscar uma pessoa na agenda.

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
    
    def get_tamanho(self):
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

    def inserir_ordenado(self, elemento):
        novo_item = Item(elemento)
        if self.is_vazia() or elemento < self.inicio.valor:
            self.inserir_inicio(elemento)
            return
        atual = self.inicio
        while atual.prox is not None and atual.prox.valor < elemento:
            atual = atual.prox
        novo_item.prox = atual.prox
        novo_item.ant = atual
        if atual.prox is not None:
            atual.prox.ant = novo_item
        atual.prox = novo_item
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
            if aux.valor[0] == item:
                return True
            aux = aux.prox
        return False

    def exibir_lista(self):
        if self.is_vazia():
            print('A lista está vazia!')
        else:
            aux = self.inicio
            while aux is not None:
                print(aux.valor[0], end=" ")
                aux = aux.prox
            print()

def menu():
    print('''
    Menu para a Agenda Telefônica
    0 - Sair
    1 - Inserir Pessoa
    2 - Remover Pessoa
    3 - Buscar Pessoa
    ''')
    op = int(input('Digite uma opção acima: '))
    funcoes(op)

def funcoes(op):
    if op == 0:
        print('Até Breve!')
        exit()
    elif op == 1:
        pessoa = input('Digite o nome e o número da pessoa separados por vírgula: ')
        nome, telefone = pessoa.split(',')
        lista.inserir_fim((nome, telefone))
        menu()
    elif op == 2:
        if lista.is_vazia():
            print('A lista está vazia')
            menu()
        else:
            pessoa = lista.remover_inicio()
            nome, telefone = pessoa
            print(f'A pessoa {nome} e seu número foram removidos!')
            menu()
    elif op == 3:
        pessoa = input('Digite o nome da pessoa que você quer procurar: ')
        if lista.buscar(pessoa):
            print(f'A pessoa {pessoa} está na lista.')
        else:
            print(f'A pessoa {pessoa} não está na lista.')
        menu()
    else:
        print('Opção inválida, tente novamente.')   
        menu()

lista = ListaEncadeadaDupla()
menu()
