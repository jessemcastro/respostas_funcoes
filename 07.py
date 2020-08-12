#Faça um programa que use a função valorPagamento para determinar
# o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação
# e o número de dias em atraso e passar estes valores para a
# função valorPagamento, que calculará o valor a ser pago e
# devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação
# e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
# que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
# cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
# juros por dia de atraso.

def valor_pagamento (vp,nd):
    resposta = vp + (vp*0.03)+(nd*0.001)
    return resposta
valor_prestacao = 1

dados = 0
quantidade = 0
valor_total = 0
while valor_prestacao != 0:
    valor_prestacao = float(input("Digite o valor da prestação"))
    numero_dias_em_atraso = float(input("Digite o numero de dias de atraso na prestação"))

    if valor_prestacao!=0:
        quantidade = quantidade + 1
        dados =  valor_pagamento(valor_prestacao,numero_dias_em_atraso)
        print(dados)
        valor_total =  valor_total + dados

print("Relatório")
print("Q = ",quantidade)
print("VT = ",valor_total)
