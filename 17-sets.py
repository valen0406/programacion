#Son una coleccion mutable de elementos inmutables, no ordenados y sin duplicados
#1 forma
# mi_set =set([1,2,3,4])
# mi_set = set({1,2,3,4})
# mi_set = set((1,2,3,4))
#2 forma

mi_set2 = {1,2,3,4}
print(type(mi_set2))

# mi_set = {1,2,3,4,5,6,1,1,1,1,1,1}
# print(mi_set)

print(len(mi_set2))

 #Conjunto con los elementos de dos conjuntos
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)



