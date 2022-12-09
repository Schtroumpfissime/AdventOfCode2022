import numpy as np
import copy

data = np.loadtxt("data.txt", dtype = "str")

longueur_corde = 10

long_tail_pos = [[0,0]]
for ii in range(longueur_corde-1):
    long_tail_pos.append([0,0])

list_pos_tail = []

def distance(head,tail):
    val = (head[0]-tail[0])**2 + (head[1]-tail[1])**2
    return val

def move_tail(head, tail):
    tail_next = tail
    dist = distance(head, tail)
    if dist <= 2:
        tail_next = tail
    elif dist == 4: #tout droit
        tail_next[0] = int((head[0]+tail[0])/2)
        tail_next[1] = int((head[1]+tail[1])/2)
    elif dist == 5 : #diagonale
        if abs(head[0]-tail[0]) > abs(head[1]-tail[1]) :
            tail_next[0] = int((head[0]+tail[0])/2)
            tail_next[1] = head[1]
        else :
            tail_next[0] = head[0]
            tail_next[1] = int((head[1]+tail[1])/2)
    else :
        if abs(head[0]-tail[0]) > 1 :
            tail_next[0] = int((head[0]+tail[0])/2)
        if abs(head[1]-tail[1]) > 1 :
            tail_next[1] = int((head[1]+tail[1])/2)
    return tail_next



for ligne in data:
    nb_steps = int(ligne[1])
    direction = 0
    sens = 1
    if ligne[0] == "U" or ligne[0] == "D" :
        direction = 1
    if ligne[0] == "L" or ligne[0] == "D" :
        sens = -1

    for ii in range(nb_steps):
        long_tail_pos[0][direction] += sens
        for jj in range(len(long_tail_pos)-1):
            long_tail_pos[jj+1] = move_tail(long_tail_pos[jj],long_tail_pos[jj+1])
        if long_tail_pos[-1] not in list_pos_tail:
            val_tmp = copy.copy(long_tail_pos[-1])
            list_pos_tail.append(val_tmp)


print("------------------------------------")
print("position tete :",long_tail_pos[0])
print("position queue :",long_tail_pos[-1])
print(len(list_pos_tail))
print("fini")