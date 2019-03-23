import random
inp = "1245"
seed = 6
hash = 0


for i in range(0,len(str(inp))):
    random.seed(i)
    hash = (hash*random.randint(0,50)) + ord(inp[i])*random.randint(0,50)
print(hash)

