import numpy as np 



data = np.loadtxt("data.txt", dtype="str")


def val_lettre(lettre):
    valeur = ord(lettre) - 96
    if valeur <= 0:
        valeur += 58
    return valeur

valeurs = []
total = 0
i_ligne = 0
for ligne in data:
    taille = int(len(ligne)/2)
    lettre_tmp = ""

    for char in range(taille):  
        if ligne[0:taille].find(ligne[taille+char]) > -1 and lettre_tmp != ligne[taille+char]:
            lettre_tmp = ligne[taille+char]
            val_tmp = val_lettre(lettre_tmp)

            total += val_lettre(ligne[taille+char])
            valeurs.append(val_lettre(ligne[taille+char]))
            continue
    i_ligne +=1        

print("total : ", total)
print("-------------------------------------------------------------------")

i_ligne = 0
total = 0
valeurs = []
lettre_tmp = ""
while i_ligne<data.size:
    ligne1 = data[i_ligne]
    ligne2 = data[i_ligne+1]
    ligne3 = data[i_ligne+2]
    taille = int(len(ligne1))

    lettre_tmp = ""

    for char in range(taille):
        if ligne2.find(ligne1[char]) > -1 and ligne1[char] != lettre_tmp:
            if ligne3.find(ligne1[char]) > -1:
                lettre_tmp = ligne1[char]
                total += val_lettre(ligne1[char])
                valeurs.append(val_lettre(ligne1[char]))
                continue
    i_ligne+=3

print("nouveau total : ", total)
