#Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.

def soma_elementos():
    lista = []
    soma = 0
    for i  in range(0,10):
        numero = int(input('Digite um número: '))
        lista.append(numero)
        soma += numero
    
    return soma

resultado = soma_elementos()
print('A soma dos elementos é: ', resultado)