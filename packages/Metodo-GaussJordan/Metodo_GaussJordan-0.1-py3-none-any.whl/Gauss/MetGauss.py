import numpy as npm

A = npm.array([[1,2],[1,4]])

B = npm.array([[3],[5]])


AB = npm.concatenate((A,B),axis=1)
AB0 = npm.copy(AB)


tamano = npm.shape(AB)
n = tamano[0]
m = tamano[1]


for i in range(0,n-1,1):
    columna = abs(AB[i:,i])
    dondemax = npm.argmax(columna)
    
    if (dondemax !=0):
        temporal = npm.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
        
AB1 = npm.copy(AB)

for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
    AB[k,:] = AB[k,:] - AB[i,:]*factor

AB2 = npm.copy(AB)

ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB[i,:] = AB[i,:]/AB[i,i]
    
X = npm.copy(AB[:,ultcolumna])
X = npm.transpose([X])


print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminacion hacia adelante')
print(AB2)
print('eliminación hacia atrás')
print(AB)
print('solución de X: ')
print(X)