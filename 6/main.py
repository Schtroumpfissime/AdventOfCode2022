import numpy as np

#data = np.loadtxt("data2.txt",dtype = "str")
data = open("data.txt","r").read()

bool_recherche = True
i = 0
sequence = ""
longueur = 14
while bool_recherche:
    sequence = data[i:i+longueur]
    if len(set(sequence))==longueur:
        bool_recherche = False
    i+=1

print(sequence, " ", i+longueur-1)