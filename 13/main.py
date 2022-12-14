import numpy as np

data = [[]]
with open("data.txt","r") as file:
    for line in file.read().splitlines():
        if line:
            data[-1].append(line)
        else:
            data.append([])


#mise en forme
def str_to_list(str):
    #liste vide
    if len(str) == 0: return[]

    liste=[]    
    if str[0] == "[" and str[-1] == "]":
        str=str[1:-1]
        if len(str) == 0: return[]
    liste = str.split(",")

    bool_recoler = False
    str_tmp=""
    ii=-1
    for ind,elem in enumerate(liste):
        if not bool_recoler: ii+=1

        if bool_recoler:
            str_tmp+=","+elem
            if str_tmp.count("[") == str_tmp.count("]"):
                bool_recoler = False 
                liste[ii] = str_to_list(str_tmp)
        else:
            if elem.isnumeric():
                liste[ii] = int(elem)
            elif elem[0] == "[" and elem[-1] == "]" and elem.count("[") == elem.count("]"):
                liste[ii] = str_to_list(elem)
            elif elem[0] == "[" and elem.count("[") != elem.count("]"):    
                bool_recoler = True
                str_tmp = elem
    if ind!=ii: 
        for jj in range(ind-ii):liste.pop(-1)

    return liste


def is_smaller(list_a, list_b):
    #0 on iter; 1 oui; 2 non
    if len(list_a)==0 and len(list_b)!=0: return 1
    if len(list_a)!=0 and len(list_b)==0: return 2

    for ii in range(min(len(list_a), len(list_b))):
        if type(list_a[ii])==int:
            if type(list_b[ii])==int:
                if list_a[ii] < list_b[ii]: return 1
                elif list_a[ii] > list_b[ii]: return 2
                else : continue
            else:
                list_a[ii] = [list_a[ii]]
        else:
            if type(list_b[ii])==int:
                list_b[ii] = [list_b[ii]]

        b_small = is_smaller(list_a[ii], list_b[ii])
        if b_small > 0:return b_small

    if len(list_a) > len(list_b): return 2
    elif len(list_a) < len(list_b): return 1
    else: return 0    

divider1 = [[2]]
divider2 = [[6]]
index1 = 1
index2 = 2

bool_part2 = False

test = 0
sum_of_indexes = 0
for ind1, ligne in enumerate(data):
    for ind2, elem in enumerate(ligne):
        data[ind1][ind2] = str_to_list(elem)

        if bool_part2:
            if is_smaller(divider2, data[ind1][ind2]) == 2:
                index2+=1
                if is_smaller(divider1, data[ind1][ind2])==2:
                    index1 +=1

    if not bool_part2:
        test = is_smaller(data[ind1][0],data[ind1][1])
        if test == 1:
            sum_of_indexes+=ind1+1
            print("couple",ind1+1,": OK. Somme =",sum_of_indexes)
        elif test == 2: 
            print("couple",ind1+1,": pas OK. Somme =",sum_of_indexes)
        else:
            print("couple",ind1+1,"PROBLEME")


if bool_part2:
    print(index1*index2)
else:
    print("somme : ", sum_of_indexes)

print("fini")