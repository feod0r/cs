import random
inp = 0
seed = 5

for j in range(1000,1010):
    hash = 0
    inp = j
    for i in range(0,len(str(inp))):
        random.seed(i)
        hash = ((hash << random.randint(0,50)) + hash) + (ord(str(inp)[i])*random.randint(0,50)<<random.randint(0,50))
    print(hash)