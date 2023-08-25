from typing import List


nova = ['abacaxi', 'morango', 'caju'] # cria-se uma List 
print (nova)

outra = tuple(nova) # Transforma a List em uma Tuple imutável
print (outra)

maisUma = list(outra) # Depois transforma a Tuple em uma List mutável
print (maisUma.append('laranja')) 
print (maisUma)

#-----------------------------------------------------------------
print("-----------------------------------------------------------")

# Tuples com dados de pessoas que são imutáveis
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

# List feita de Tuples
instrutores = [pessoa1, pessoa2, pessoa3]
print (instrutores)

# Para achar elementos na List de Tuples, primeiro se usa o número de local da List, depois a do Tuple
print (instrutores[2][1])