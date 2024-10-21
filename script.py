import array as ar
import random

N = ar.array('f', [0.0]* 5) 
for i in range(len(N)):
    N[i] = 3**i
    
random.shuffle(N)

for el in N:
    print(el)
