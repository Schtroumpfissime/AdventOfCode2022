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
                    
                    liste_dossier.append([dossier_actuel,contenu_dossier_actuel, chemin[:]])
                    
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

liste_dossier.append([dossier_actuel,contenu_dossier_actuel, chemin])


poids_leger = 0
liste_poids = []
liste_dossier_rev = list(reversed(liste_dossier))

compteur = 0

for dir in liste_dossier_rev:
    poids_tmp = 0

    for element in dir[1]:
        if element.isdigit():
            poids_tmp += int(element)
        else :
            test = 0            
            for dir_tmp, ele_tmp, parent_tmp in reversed(liste_poids):
                if element == dir_tmp and parent_tmp[0:-1] == dir[2]:
                    poids_tmp += int(ele_tmp)
                    test +=1
                    
            if test != 1:
                print("Pas de ", element, " avec pour parent ", dir[2])
                    

    liste_poids.append([dir[0], poids_tmp, dir[2]])
    if poids_tmp <= 100000:
        poids_leger += poids_tmp
    compteur +=1
  #  print("--> le dossier ", liste_poids[-1][0], " pèse ", liste_poids[-1][1])

print("---------------------------------------------------")
print("somme des poids légers :" ,poids_leger)

poids_min_a_suppr = liste_poids[-1][1] - 40000000
poids_a_suppr = 70000000
dossier = ""
for dir, pds, par in liste_poids:
    if pds>=poids_min_a_suppr and pds < poids_a_suppr:
        poids_a_suppr = pds
        dossier = dir

print("---------------------------------------------------")
print("poids total : ", liste_poids[-1][1])
print("poids min : ", poids_min_a_suppr)
print("dossier : ", dossier)
print("poids à supprimer : ",poids_a_suppr)