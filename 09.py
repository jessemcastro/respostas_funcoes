#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.

def quantidade (numero):
    tamanho = (str(numero))
    tamanho = tamanho[::-1]
    return tamanho
numero = int(input("Digite um numero"))

print("o numero possui",quantidade(numero),"digitos")