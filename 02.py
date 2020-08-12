#Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir (numero):
    resposta = ''
    anterior = ''
    parada_laco1 = numero + 1

    for laco1 in range(1,parada_laco1):
        parada_laco2 = laco1 + 1

        for laco2 in range (1, parada_laco2):

            resposta = resposta + str(laco2)

        resposta = resposta + "\n"
    print(resposta)

numero = int(input("Digite um numero inteiro"))
imprimir(numero)