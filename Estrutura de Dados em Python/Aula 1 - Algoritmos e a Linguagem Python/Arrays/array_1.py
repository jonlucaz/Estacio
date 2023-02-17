import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

nomes = ["João", "Maria", "José"]
print(nomes)
print(nomes[1])
print(len(nomes))

for x in nomes:
    print(x)

nomes.append("Carlos")
print(nomes)
nomes.remove("João")
print(nomes)
nomes.remove(nomes[1])
print(nomes)
nomes.pop(0)
print(nomes)
