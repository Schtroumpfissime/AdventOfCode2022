import numpy as np

data = np.loadtxt("data.txt", dtype = "str", delimiter = ",")

compteur1 = 0
compteur2 = 0
for ligne in data:
    range1 = [int(d) for d in ligne[0].split("-")]
    range2 = [int(d) for d in ligne[1].split("-")]

    if (range1[0]>=range2[0] and range1[1]<=range2[1]) or (range1[0]<=range2[0] and range1[1]>=range2[1]):
        compteur1 +=1

    if max(range1[0], range2[0]) <= min(range1[1], range2[1]):
        compteur2+=1



print(compteur1)
print(compteur2)