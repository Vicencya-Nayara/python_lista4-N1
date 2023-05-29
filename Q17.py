#Implemente uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings que possuem mais de 5 caracteres.

def strings():
    lista = []
    for i in range(0,5):
        string = input('Digite uma string: ')
        lista.append(string)
    
    strings_fil = [string for string in lista if len(string) > 5]
    return strings_fil

resultado = strings()
print('As strings com mais de 5 caracteres são: ', resultado)
