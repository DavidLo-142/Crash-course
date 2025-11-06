#List
list=[10, 20, 30]
#     0   1   2

liste = list
liste.append("one")
list.append("two")

correct_liste = liste
correct_liste[-4]="twenty"
#print(liste)
#print(list)
#print(len(list))

list_a=[1,2,3]
list_b=[4,5,6]
list_c=[list_a, list_b]
print(list_c)
#list_c = [[1,2,3],[4,5,6]]
#           0 1 2   0 1 2 
print(list_c[0])
print(list_c[1])

