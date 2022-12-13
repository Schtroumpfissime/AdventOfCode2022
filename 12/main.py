import numpy as np
import copy
import math

data = np.loadtxt("data.txt", dtype = "str")


length = len(data[0])
width = len(data)
for ii in range(width):
    if "S" in data[ii]:
        depart = [ii,data[ii].find("S")]
    if "E" in data[ii]:
        arrivee = [ii,data[ii].find("E")]


distances_relatives = [[math.inf]*(width*length)]
coord_S = depart[0]*length + depart[1]
coord_Z = arrivee[0]*length + arrivee[1]
distances_relatives[0][coord_Z]=0


def val_alpha(coord):
    str_tmp = data[coord[0]][coord[1]]
    if str_tmp == "S":
        str_tmp = "a"
    elif str_tmp == "E":
        str_tmp = "z"
    return ord(str_tmp)

def cases_voisines(pos,bool_up):
    list_pos = []
    a = val_alpha(pos)
    for ii in [-1,1]:
        for i_bool in [True, False]:
            new_pos = [pos[0]+i_bool*ii, pos[1]+(not i_bool)*ii]
            if new_pos[0] in range(width) and new_pos[1] in range(length):                
                b = val_alpha(new_pos)
                if bool_up and a >= (b-1):
                    list_pos.append(new_pos)
                elif not bool_up and a <= (b+1):
                    list_pos.append(new_pos)
    return list_pos


coord_lineaire = coord_Z
case_trouvee = [coord_lineaire]
for ii in range(width*length-1):
    list_dist = distances_relatives[-1][:]

    distance_au_depart = distances_relatives[ii][coord_lineaire]

    coord = [coord_lineaire//length , coord_lineaire%length]

    voisines = cases_voisines(coord,False)
    for vois in voisines:
        co_lin = vois[0]*length + vois[1]
        list_dist[co_lin] = min(list_dist[co_lin],distance_au_depart+1)

    list_tmp = copy.copy(list_dist)
    for ii in case_trouvee: list_tmp[ii] = math.inf
        

    coord_lineaire = np.argmin(list_tmp)
    distances_relatives.append(list_dist)
    case_trouvee.append(coord_lineaire)


#on cherche tous les a
list_a = []
for index1,ligne in enumerate(data):
    for index2,lettre in enumerate(ligne):
        if lettre == "a":
            list_a.append(index1*length + index2)

min_dist = math.inf
for aa in list_a:
    min_dist = min(min_dist,distances_relatives[-1][aa])
print("distance minimale",min_dist)

#print(distances_relatives[-1][coord_Z])
print("fini")