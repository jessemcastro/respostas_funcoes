#Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

def estado (numero):
    if numero > 0:
        resposta = "P"
    elif numero<0:
        resposta = "N"
    else:
        resposta = "Número 0"
    return resposta

numero = int(input("Digite um numero"))
print(estado(numero))

