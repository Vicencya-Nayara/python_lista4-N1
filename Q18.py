#Crie uma função que receba duas listas de números e retorne uma nova lista contendo apenas os 
#elementos que estão presentes em ambas as listas.

def elementos_comuns():
    lista1 = []
    lista2 = []

    n = int(input('Digite a quantidade de números da primeira lista: '))
    print('Digite os números da lista1: ')

    for i in range(n):
        numero = int(input())
        lista1.append(numero)

    m = int(input('Digite a quantidade de números da segunda lista: '))
    print('Digite os números da lista2: ')

    for i in range(m):
        numero = int(input())
        lista2.append(numero)
    
    comuns = [elemento for elemento in lista1 if elemento in lista2]
    return comuns

resultado = elementos_comuns()
print('Elementos comuns nas duas listas:', resultado)

