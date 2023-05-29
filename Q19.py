#Implemente uma função que receba uma lista de palavras e retorne a palavra mais longa presente na lista.

def palavra_mais_longa():
    lista_palavras = input('Digite as palavras: ').split()
    palavra_mais_longa = " "

    for palavra in lista_palavras:
        if  len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    return palavra_mais_longa

palavra_longa = palavra_mais_longa()
print('A palavra mais longa é: ', palavra_longa)
