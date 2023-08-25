# Suponha que tenhamos uma lista com os seguintes inteiros:

inteiros = [1,3,4,5,7,8]

# queremos preencher uma nova lista com o quadrado de cada número 
# da lista anterior, Considerando que, para calcular o quadrado de um número, fazemos x*x
# através do recurso List Comprehension.

quadrados = [n*n for n in inteiros]
print (quadrados)

# O recurso List Comprehension também permite utilizar condições para o 
# preenchimento da lista. Considere o objetivo de inicializar uma 
# lista com os números pares a partir de uma lista de números inteiros qualquer, 
# por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição 'numero % 2 == 0'

inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

# O código usando List Comprehension relativo ficaria muito mais compacto:

inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]        
print (pares)

# Repare o if depois do for que define a condição