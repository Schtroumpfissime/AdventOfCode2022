import numpy as np

data = [[]]
with open("data.txt","r") as fichier:
    for line in fichier.read().splitlines():
        if line:
            data[-1].append(line)
        else:
            data.append([])

nb_stacks = int(data[0][-1][-2])
stacks = [[]]
pile_max = len(data[0])-1
for i in range(nb_stacks):
    stacks.append([])
    for j in range(pile_max):
        lettre = data[0][pile_max-j-1][4*i+1]
        if lettre!=" ":
            stacks[i].append([])
            stacks[i][j] = lettre
stacks.pop(-1)


def deplacer(tas,nombre,pile1,pile2):
    taille1 = len(tas[pile1])
    taille2 = len(tas[pile2])
    for i in range(nombre):
        tas[pile2].append([])
        tas[pile2][taille2+i] = tas[pile1][taille1-i-1]
        tas[pile1].pop(-1)
    return tas

def deplacer2(tas,nombre,pile1,pile2):
    taille1 = len(tas[pile1])
    taille2 = len(tas[pile2])
    for i in range(nombre):
        tas[pile2].append([])
        tas[pile2][taille2+i] = tas[pile1][taille1-nombre+i]
    for i in range(nombre):
        tas[pile1].pop(-1)
    return tas


for ligne in data[1]:
    instruction = ligne.split(" ")
    deplacer2(stacks,int(instruction[1]),int(instruction[3])-1,int(instruction[5])-1)


dessus = ""
for ligne in stacks:
    dessus += ligne[-1]

print(dessus)