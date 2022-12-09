import numpy as np

data = np.loadtxt("data.txt", dtype="str")

trad = {"A":1, "X":1, "B":2, "Y":2, "C":3, "Z":3}

def score(round):
    sa_forme, ma_forme = (trad[d] for d in round)
    total = ma_forme
    if sa_forme == ma_forme:
        total +=3
    if (ma_forme - sa_forme)%3 == 1:
        total +=6
    return total

sum = np.sum([score(d) for d in data])

print(sum)

valeur = [1,2,3]
def new_score(round):
    sa_forme, resultat = (trad[d] for d in round)
    total = (resultat-1)*3 #victoire
    total += valeur[(sa_forme + resultat)%3] #forme
    return total

sum2 = np.sum([new_score(d) for d in data])

print("opti : ",sum2)