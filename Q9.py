#Um banco precisa armazenar as informações dos clientes em uma lista encadeada simples. 
#Cada cliente possui nome, número da conta e saldo. Implemente as operações de inserir, 
#remover e esquisar um cliente na lista. A cada operações, mostrar a lista em “formado de tabela”.

class Cliente:
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.proximo = None
        
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def vazia(self):
        return self.cabeca is None

    def inserir_inicio(self, nome, conta, saldo):
        novo_cliente = Cliente(nome, conta, saldo)
        novo_cliente.proximo = self.cabeca
        self.cabeca = novo_cliente
        self.tamanho += 1

    def inserir_fim(self, nome, conta, saldo):
        novo_cliente = Cliente(nome, conta, saldo)
        if self.vazia():
            self.cabeca = novo_cliente
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_cliente
        self.tamanho += 1

    def remover(self, nome):
        if self.vazia():
            return False

        if self.cabeca.nome == nome:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True

        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.nome == nome:
                anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def pesquisar(self, nome):
        atual = self.cabeca
        while atual is not None:
            if atual.nome == nome:
                return atual
            atual = atual.proximo
        return None

    def exibir_lista(self):
        if self.vazia():
            print("A lista está vazia!")
        else:
            print("{:<15} {:<15} {:<10}".format("Nome", "Conta", "Saldo"))
            print("------------------------------------")
            atual = self.cabeca
            while atual is not None:
                print("{:<15} {:<15} {:<10.2f}".format(atual.nome, atual.conta, atual.saldo))
                atual = atual.proximo


def cliente():
    lista_clientes = ListaEncadeada()

    while True:
        print("\n--- Banco do Brasil ---")
        print("1. Inserir cliente")
        print("2. Remover cliente")
        print("3. Pesquisar cliente")
        print("4. Exibir lista")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            conta = input("Número da conta: ")
            saldo = float(input("Saldo: "))
            lista_clientes.inserir_fim(nome, conta, saldo)
            print("Cliente inserido com sucesso!")

        elif opcao == "2":
            if lista_clientes.vazia():
                print('A lista está vazia')
            else:
                nome = input('Digite o nome do cliente que deseja remover: ')
                if lista_clientes.remover(nome):
                    print('Cliente removido com sucesso')
                else:
                    print('Cliente não encontrado')

        elif opcao == "3":
            if lista_clientes.vazia():
                print('A lista está vazia')
            else:
                nome = input('Digite o nome do cliente que deseja pesquisar: ')
                cliente = lista_clientes.pesquisar(nome)
                if cliente is not None:
                    print('Cliente encontrado:')
                    print(f"Nome: {cliente.nome}")
                    print(f"Conta: {cliente.conta}")
                    print(f"Saldo: {cliente.saldo}")
                else:
                    print('Cliente não encontrado')

        elif opcao == "4":
            lista_clientes.exibir_lista()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

cliente()
