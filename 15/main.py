import numpy as np
import re
import math

def distance(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

b_part2 = True

data = []
distances = []
list_inter = [[]]

if b_part2:
    row_min = 0
    row_max = 4000000
else : 
    row_min = row_max = 2000000

print('Lecture fichier')

with open("data.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            list_tmp = [int(s) for s in re.findall(r'-?\d+', line)]
            data.append(list_tmp)

            dist = distance(*list_tmp)
            distances.append(dist)

print('Détection intervalles')

for jj,row in enumerate(range(row_min,row_max+1)):
    list_inter.append([])
    for ii,sensor in enumerate(data):
        dist = distances[ii]
        dist_to_row = abs(sensor[1]-row)
        
        if dist >= dist_to_row:
            min_tmp = sensor[0] - (dist - dist_to_row)
            max_tmp = sensor[0] + (dist - dist_to_row)
                                
            list_inter[jj].append([min_tmp,max_tmp])
    if jj%400000 == 0: print(100*jj/row_max,'%')
list_inter.pop(-1)
            
print('Simplification intervalles')

for kk,row in enumerate(range(row_min,row_max+1)):
    list_inter[kk].sort()
    intervals = [list_inter[kk][0]]
    for ii in list_inter[kk][1:]:
        for ind,jj in enumerate(intervals):
            if min(ii[1],jj[1]) >= max(ii[0],jj[0]):
                intervals[ind][1] = max(intervals[ind][1], ii[1])
                intervals[ind][0] = min(intervals[ind][0], ii[0])
            else:
                intervals.append(ii)
    if b_part2 and len(intervals) > 1: 
        x= intervals[0][1]+1
        print("trouvé en ", x, row)
        print("ça fait : ", x*4000000 + row)
        break
    if kk%400000 == 0: print(100*kk/row_max,'%')

if not b_part2:
    print('Supression des balises')
    surlaligne = []
    nombre = 0 
    for inter in intervals:
        for sensor in data:    
            for ii in range(2):
                if sensor[ii*2+1] == row and (inter[0] <= sensor[ii*2] <= inter[1]) and sensor[2*ii:2*ii+1] not in surlaligne:
                    surlaligne.append(sensor[2*ii:2*ii+1])
        nombre +=  inter[1] - inter[0] + 1
    nombre -= len(surlaligne)
    print("positions sans balises : ",nombre)


print("fini")