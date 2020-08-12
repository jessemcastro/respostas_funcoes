#Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de
# custo para incluir o imposto sobre vendas.

def chama_imposto(taxaImposto, custo):

    conversao_taxaImposto = taxaImposto/100
    resposta = custo + (conversao_taxaImposto * custo)
    return resposta

taxa = float(input("Digite o valor da taxa, EX: 30 para 30%"))
custo_sem_imposto = float(input("Digite o custo do produto"))
custo_com_imposto = chama_imposto(taxa,custo_sem_imposto)
print("O novo custo será de:",custo_com_imposto)
