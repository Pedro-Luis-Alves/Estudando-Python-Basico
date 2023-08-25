# Set é uma coleção que não permite valores duplicados

# Usamos chaves '{}' para declarar o Set
colecao = {11122233344, 22233344455, 33344455566} 

colecao.add(44455566677) #vai adicionar pois não existe ainda
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!

# É importante notar que o set não é uma sequência, pois não tem um índice.
# E como não temos um índice não sabemos em qual ordem vem os valores quando 
# imprimimos um set de dentro de um laço for:

for cpf in colecao:
     print(cpf)

# Os elementos foram listados fora da ordem de inserção. Isso acontece porque o set não é ordenado.