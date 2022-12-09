import numpy as np

data = [[]]

chemin = []
dossier_actuel = "/"
contenu_dossier_actuel = []
liste_dossier = []


with open("data.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            ligne = line.split(" ")
            if ligne[0] == "$": #commande
                if len(contenu_dossier_actuel)>0: #fin de ls
                    if len(chemin)>1:
                        liste_dossier.append([dossier_actuel,contenu_dossier_actuel, chemin[-2]])
                    else :
                        liste_dossier.append([dossier_actuel,contenu_dossier_actuel, "/"])
                    contenu_dossier_actuel = []

                """ if ligne[1] == "ls":
                    compteur+=1 """
                if ligne[1] == "cd":
                    if ligne[2] == "..":
                        chemin.pop(-1)
                    else:
                        chemin.append(ligne[2])
                        dossier_actuel = ligne[2]
                    
            elif ligne[0] == "dir": #dossier
                contenu_dossier_actuel.append(ligne[1])
            else : #fichier
                contenu_dossier_actuel.append(ligne[0])

liste_dossier.append([dossier_actuel,contenu_dossier_actuel, chemin[-2]])



def poids_dossier(str_dossier):
    poids = 0
    for dir, files in liste_dossier:
        if dir == str_dossier:
            for i in files:
                if i.isdigit():
                    poids += int(i)
                else :
                    poids += poids_dossier(i)
    return poids

poids_leger = 0
for dir in liste_dossier :
    poids_tmp = poids_dossier(dir[0])
    if poids_tmp <= 100000:
         poids_leger += poids_tmp







poids_min_a_suppr = 70000000 - liste_poids[-1][1]
poids_a_suppr = 70000000
dossier = ""
for dir, pds, par in liste_poids:
    if pds>=poids_min_a_suppr and pds < poids_a_suppr:
        poids_a_suppr = pds
        dossier = dir

print("---------------------------------------------------")
print("poids min : ", poids_min_a_suppr)
print("dossier : ", dossier)
print(poids_a_suppr)




print("fini")