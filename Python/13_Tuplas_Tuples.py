# 'Tuplas' ou 'Tuples' são listas imutaveis, fixas, não podem se alteradas

semana = ["D", "S", "T", "Q", "Q", "S", "S"] # Lista comum
print (semana.append("S2")) # Adiciona um valor a lista
print (semana.pop()) # Mostra o ultimo valor da lista

#------------------------------------------------------------------------

dias = ("D", "S", "T", "Q", "Q", "S", "S") # Lista Tuple, se diferencia com o uso de parênteses '()'
print (dias.append("S2")) # Tenta adicionar um valor a lista, mas dá erro
print (dias.pop()) # Tenta mostrar o ultimo valor da lista, mas dá erro

# Importante saber que existem algumas funções que funcionam com todos os tipos 
# de sequências como os built-ins: len, min e max.

print (dias.max() , semana.max()) # Tenta mostrar o ultimo valor da lista, mas dá erro