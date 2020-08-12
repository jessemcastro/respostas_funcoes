#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
# como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
# conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos
# valores de entrada todas as vezes que desejar.

def converter (horas,minutos):
    if horas>12:
        nova_hora = horas - 12
        turno = 'PM'

    elif horas<=12:
        nova_hora = horas
        turno = 'AM'

    return nova_hora,minutos,turno

def saida (hora,minuto,turno):
    print(hora,":",minuto,":",turno)

continuar = 's'

while continuar == 's':



    informar_hora = int(input("Digite as horas, ex:##\n"))

    informar_minuto = int(input("Digite os minutos, ex: ##\n"))



    horario_convertido = converter(informar_hora,informar_minuto)
    saida(horario_convertido[0],horario_convertido[1],horario_convertido[2])
    continuar = input("Deseja continuar ? s ou n")
