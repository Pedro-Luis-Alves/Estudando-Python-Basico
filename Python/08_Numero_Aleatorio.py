import random # Inportando random

num = random.random(); # sempre cria um float
print (num)

num = int(random.random() * 100); # sempre cria um float que é convertido para INT
print (num)

num = random.randrange(1, 101); # Define um número mainimo e um número limite
print (num)