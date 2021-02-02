from itertools import combinations


lista = [1,2,3,4,5,6,7,8,9]

resultado = list(combinations(lista,3))
resultado1 = resultado[0][0]

print (resultado)
print (resultado1)