#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

def quantidade (numero):
    tamanho = len(str(numero))
    return tamanho
numero = int(input("Digite um numero"))

print("o numero possui",quantidade(numero),"digitos")

