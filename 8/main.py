import numpy as np

data = np.loadtxt("data.txt", dtype = "str")
foret = []
for ligne in data:
    foret.append([int(a) for a in str(ligne)])
foret = np.array(foret)

taille = len(foret)
arbres_visibles = 4*(taille-1)
scenic_score = 0

for ii in range(1, taille-1):
    for jj in range(1, taille-1):
        val_arbre = foret[ii,jj]
        if val_arbre > max(foret[0:ii,jj]) or val_arbre > max(foret[ii+1:,jj]) or\
             val_arbre > max(foret[ii,0:jj]) or val_arbre > max(foret[ii,jj+1:]):
            arbres_visibles += 1

        scenic_tmp = 1

        val_tmp = np.where(foret[0:ii,jj] >= val_arbre)
        if len(val_tmp[0])>0:
            scenic_tmp *= (ii -val_tmp[0][-1])  
        else :
            scenic_tmp *= ii

        val_tmp = np.where(foret[ii+1:,jj] >= val_arbre)
        if len(val_tmp[0])>0:
            scenic_tmp *= (val_tmp[0][0]+1)
        else :
            scenic_tmp *= (taille-ii-1)

        val_tmp = np.where(foret[ii,0:jj] >= val_arbre)
        if len(val_tmp[0])>0:
            scenic_tmp *= (jj-val_tmp[0][-1])
        else :
            scenic_tmp *= jj

        val_tmp = np.where(foret[ii,jj+1:] >= val_arbre)
        if len(val_tmp[0])>0:
            scenic_tmp *= (val_tmp[0][0]+1)
        else :
            scenic_tmp *= (taille-jj-1)

        scenic_score = max(scenic_score,scenic_tmp)

print("On peut voir", arbres_visibles, "arbres")

print("le meilleur score est", scenic_score)

print("fini")