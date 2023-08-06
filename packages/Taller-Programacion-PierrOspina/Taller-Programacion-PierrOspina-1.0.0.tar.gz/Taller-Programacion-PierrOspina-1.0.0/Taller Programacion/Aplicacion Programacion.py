#Jean Pierr Ospina Jimenez
#Taller Programacon II
#Trabajo y manejo de matrices con operaciones basicas en phyton con numpy

import numpy as np

#Acceder a los elementos de una matriz
#Matriz normal
W = np.array([2, 4, 6, 8, 10])
print("Matriz Prueba 1 =", W)
print("W[0] =", W[0])         #Primer elemento
print("W[2] =", W[2])         #Tercer elemento
print("W[-1] =", W[-1])       #Ultimo elemento

print("-----------------------------------------------------------")

#Matriz bidireccional

X = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
print("Matriz Prueba 2 =", X)

#Primer elemento de la primera fila
print("X[0][0]] =", X[0][0])

#Tercer elmento de la segunda fila
print("X[1][2] =", X[1][2])

#Ultimo elemento de la ultima fila
print("X[-1][-1] =", X[-1][-1])

print("-----------------------------------------------------------")

#Accediendo a las filas de una matriz

print("Acceder a las filas de una matriz")

Y = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
print("Matriz Y =", Y)

#Primera fila
print("Primera fila de la matriz =", Y[0])

#Tercera fila
print("Tercera fila de la matriz =", Y[2])

#Ultima fila
print("Ultima fila de la matriz =", Y[-1])

print("-----------------------------------------------------------")

#Accediendo a las columnas de una matriz

print("Acceder a las columnas de la matriz")

Z = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
print("Matriz Z =", Z)

#Primera columna
print("Primera columna de la matriz =", Z[:,0])

#Tercera columna
print("Tercera columna de la matriz =", Z[:,2])

#Ultima columna
print("Ultima columna de la matriz =", Z[:,-1])

print("-----------------------------------------------------------")

#Suma dos matrices y crea una tercera con el resultado de esta
print("Suma de matrices")
A = np.array([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[5, 8, 1], [6, 7, 3], [4, 5, 9]])
result = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print("Matriz A =",A)
print("Matriz B =",B)
#Itera a travez de las filas
for i in range(len(A)):
    #Itera a travez de las columnas
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print("Resultado =", r)

print("-----------------------------------------------------------")

#Multiplicacion de dos matrices y crear una tercera con el resultado de esta
print("Multiplicacion de matrices")
C = np.array([[3, 6, 7], [5, -3, 0]])
D = np.array([[1, 1], [2, 1], [3, -3]])
E = C.dot(D)
print("Matriz C =", C)
print("Matriz D =", D)
print("Resultado =", E)

print("-----------------------------------------------------------")

#Resta de dos matrices y crear una tercera con el resultado de esta
print("Resta de matrices")
F = np.array([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
G = np.array([[5, 8, 1], [6, 7, 3], [4, 5, 9]])
result = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print("Matriz F =",F)
print("Matriz G =",G)
#Itera a travez de las filas
for i in range(len(F)):
    #Itera a travez de las columnas
    for j in range(len(F[0])):
        result[i][j] = F[i][j] - G[i][j]

for R in result:
    print("Resultado =", R)

