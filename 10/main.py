import numpy as np

#data = np.loadtxt("data2.txt", dtype = "str", delimiter = None)


data = [[]]
list_register = []
current_register = 1
with open("data.txt","r") as file:
    for line in file.read().splitlines():
        ligne = line.split(" ")
        data[-1].append(ligne)
        if len(ligne) == 1:
            list_register.append(current_register)
        else :
            list_register.append(current_register)
            list_register.append(current_register)
            current_register += int(ligne[1])
            
array_register = np.array(list_register)
liste_cycles = np.array([20,60,100,140,180,220])
#print(array_register[liste_cycles -1])
#print(array_register[liste_cycles-1]*liste_cycles)
print(sum(array_register[liste_cycles-1]*liste_cycles))

screen = ""
for i_cycle in range(len(array_register)):
    pixel = i_cycle%40
    if abs(pixel - list_register[i_cycle]) <= 1 :
        screen+="#"
    else :
        screen+="."


for ii in (liste_cycles -20):
    print(screen[ii:ii+40])
print("fini")