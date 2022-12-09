import numpy as np


data = [[]]
with open("data.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            data[-1].append(int(line))
        else:
            data.append([])

sums = np.array([np.sum(d) for d in data])

print(np.max(sums))

print(np.sum(np.sort(sums)[-3:]))

