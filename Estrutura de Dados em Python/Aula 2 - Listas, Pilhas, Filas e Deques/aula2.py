# Lista em alocação contígua
# Lista éa estrutura de dados mais simples
#Uma lista (também chamada de lista linear) é um conjunto de itens organizados sequencialmente (também chamados de nós),
# que, geralmente, guardam alguma relação entre si.
nomes =["João", "Maria", "Ana"]
i = nomes.index("João")         #busca o índice do nó com a chave Joao
print(i)

nomes.append("Arthur")       #insere um novo nó contendo Arthur
print(nomes)
nomes.remove('Arthur') #remove o nó indicado
print(nomes)
nomes.pop(2) #remove o nó no indice indicado
print(nomes)
nomes.pop() #remove o último indice
print(nomes)


# Lista em alocação encadeada
# Conceito: Essa estrutura permite que os nós estejam salvos em espaços não contíguos da memória, espalhados por diversos
# endereços distantes entre si, mas que, ainda assim, seja possível percorrer a lista sem se perder.



