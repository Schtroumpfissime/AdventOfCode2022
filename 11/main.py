import numpy as np
import math as math

operations = [[]]
liste_objets = [[]]
with open("data2.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            if "Starting items:" in line:
                list_tmp = line[18:].split(", ")
                for ii in list_tmp:
                    liste_objets[-1].append(int(ii))
            elif "Operation:" in line:
                operations[-1].append(line.split(" ")[-2:])
            elif "Test: divisible by" in line:
                operations[-1].append(int(line.split(" ")[-1]))
            elif "If true: throw to monkey" in line:
                operations[-1].append(int(line.split(" ")[-1]))
            elif "If false: throw to monkey" in line:
                operations[-1].append(int(line.split(" ")[-1]))
        else:
            liste_objets.append([])
            operations.append([])


def calcul(old_val,list_str):
    if "old" in list_str[1]:
        val = old_val
    else:
        val = int(list_str[1])
    if "+" in list_str[0]:
        resultat = old_val+val
    else:
        resultat = old_val*val
    return resultat




compteur_inspection=[0]*len(liste_objets)
modulo = 1
for ii in operations:
    modulo *= ii[1]

for i_round in range(10000):
    for i_monk in range(len(liste_objets)):
        for i_objet in range(len(liste_objets[i_monk])):
            new_val = calcul(liste_objets[i_monk][0],operations[i_monk][0])
            #new_val= math.floor(new_val/3)
            new_val= new_val%modulo
            if new_val%operations[i_monk][1] == 0:
                liste_objets[operations[i_monk][2]].append(new_val)
            else:
                liste_objets[operations[i_monk][3]].append(new_val)

            liste_objets[i_monk].pop(0)
            compteur_inspection[i_monk]+=1
    if i_round%1000 == 0:
        print(compteur_inspection)

print(compteur_inspection)
test = np.sort(compteur_inspection)[-2:]
print(test)
#test2 = np.prod(test)
#test2 = long(test[0])*long(test[1])
#print("solution = ",test2)
#print(52166*52013)
print("fini")