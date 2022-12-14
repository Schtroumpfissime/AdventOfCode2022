import numpy as np
import copy


data = [[]]
minx = 500
maxx = 500
maxy = 0
b_part2 = True

#lecture
with open("data.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            list_str = line.split(" -> ")
            for ii in list_str:
                coord = ii.split(",")
                x = int(coord[0])
                minx = min(minx,x)
                maxx = max(maxx,x)                
                y = int(coord[1])
                maxy = max(maxy,y)
                data[-1].append([x,y])        
            data.append([])
    data.pop(-1)

#initialisation des caillous
if b_part2:
    maxy+=2
    width = 2*(maxy+int((maxx-minx +1)/2))
    offsetx = minx -int((width-maxx + minx -1)/2)
else:
    width = maxx-minx +1
    offsetx = minx

def afficher_cave(matrice):
    for ligne in matrice:
        str_tmp = ""
        for elem in ligne:
            if int(elem) == 0:str_tmp+="."
            elif int(elem) == 1:str_tmp+="#"
            elif int(elem) == 2:str_tmp+="o"
        print(str_tmp)
    return


cave = np.zeros((maxy+1,width))
for ligne in data:
    for ii in range(len(ligne)-1):
        for axe in range(2):
            if ligne[ii][axe] == ligne[ii+1][axe]:
                test = ligne[ii+1][1-axe] - ligne[ii][1-axe]
                if test <0:test=-test
                for jj in range(test+1):
                    abs = min(ligne[ii][0],ligne[ii+1][0]) +axe*jj
                    ord = min(ligne[ii][1],ligne[ii+1][1]) +(1-axe)*jj
                    cave[ord][abs -offsetx] = 1
if b_part2:
    for ii in range(len(cave[-1])):
        cave[-1][ii] = 1

def new_pos(pos):
    new = copy.copy(pos)
    #if pos[1] >= maxy: return new
    if cave[pos[1]+1][pos[0]] == 0:
        new[1] += 1
    elif pos[0] > 0 and cave[pos[1]+1][pos[0]-1] == 0:
        new[1] += 1
        new[0] -= 1 
    elif pos[0] < width-1 and cave[pos[1]+1][pos[0]+1] == 0:
        new[1] += 1
        new[0] += 1
    return new


pas_tombe = True
pos_grain_init = [500-offsetx,0]
pos_grain = copy.copy(pos_grain_init)
last_pos = [0,0]
nb_grains = 0
secu = 0
while pas_tombe:

    if pos_grain == last_pos:
        if b_part2 and pos_grain==pos_grain_init:
            pas_tombe = False
            print("ça touche le haut")
        if pos_grain[0] in [0,width-1] :
            pas_tombe = False
            print("ça sort sur le côté, à la profondeur",pos_grain[1])
        else:
            cave[pos_grain[1],pos_grain[0]] = 2
            pos_grain = copy.copy(pos_grain_init)
            nb_grains+=1
    elif pos_grain[1] >= maxy:
        pas_tombe = False
        print("ça tombe par le bas")
    else:
        last_pos = pos_grain
        pos_grain = new_pos(pos_grain)
      
    if nb_grains> ((len(cave)-1)**2):
        pas_tombe = False
        print("problème : peut pas y avoir autant de sable")



milieu = int(len(cave[0])/2)
afficher_cave(cave[:,:milieu])
print("---------------------------------------------------------------------")
afficher_cave(cave[:,milieu:])

print(nb_grains,"grains de sables sont tombés")

print("fini")