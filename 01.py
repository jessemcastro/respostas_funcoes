#Faça um programa para imprimir:
# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ...


def imprimir(numero):

    parada_1 = numero + 1
    resposta = ''

    for laco_1 in range (1,parada_1):
        parada_2 = laco_1 + 1
        for laco_2 in range(1, parada_2):
            resposta = resposta + str(laco_1)
        resposta = resposta + "\n"
    print(resposta)

imprimir(3)
