# Código de: '14_Liste_&_Tuples'

# Tuples com dados de pessoas que são imutáveis
pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

# List feita de Tuples
instrutores = [pessoa1, pessoa2, pessoa3]
print (instrutores)

# Para achar elementos na List de Tuples, primeiro se usa o número de local da List, depois a do Tuple
print (instrutores[2][1])

print("-----------------------------------------------------------")

# Agora vem o problema: E se não sabemos a posição do Flavio? 
# Em geral, como podemos descobrir a idade de um instrutor sem saber a posição dele?
# Repare que temos, na nossa coleção, sempre um nome associado com a idade. Sempre temos um par de valores

# Invés de usar a posição gostaria de descobrir a idade através do nome, para isso é 
# preciso usar uma nova estrutura de dados, o Dictionary!

# Para criar um dicionário devemos inicializar os instrutores de um modo um pouco diferente. 

instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}

# Repare que usamos as chaves {} (como se fosse um set), mas sempre tem em pares.
# Nesse par, temos no lado esquerdo a chave e no lado direito o valor. Isso é importante pois 
# usamos a chave para recuperar um valor e assim resolvemos nosso problema

instrutores['Flavio']

# Em resumo, o valor à esquerda serve como uma chave para achar o valor à direita.