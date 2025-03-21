import numpy as np

n=15 # tamaño de los vectores

# declarando los arreglos a utilizar
a= n*[2];
b= n*[4];

a=np.array(a);
b=np.array(b);
c=np.zeros_like(a);

#print(type(a)) #visualizacion de la lista

for i in range(n):
	c[i]=a[i]+b[i]

print("el resultado es",c)

import numpy as np

n=3 # tamaño de los vectores

# declarando los arreglos a utilizar
A= n*[n*[2]];
B= n*[n*[4]];

A=np.array(A)
B=np.array(B)
C=np.zeros_like(A)

for i in range(n):
	for j in range(n):
		C[i,j]=A[i,j]+B[i,j]

print(C)
