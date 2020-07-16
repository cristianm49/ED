

notas = [[[2.4,2.4,3.4],[3.2,4.7,3.3],[2.4,2.4,5.0]],
[[2.5,3.4,5.0],[2.3,4.3,4.3],[5.0,3.2,5.0]]]
contadorarreglo= double(0)

for (int i = 0; i < dimension; i++)
contadorFilas= double(0)
contadorcolumnas= double(0)
contadorprofundidad= double(0)

for (int j = 0; j < dimension; j++) 

for (int k = 0; k < dimension; k++) 
contadorFilas= contadorFilas + notas[i][j][k]
contadorcolumnas = contadorcolumnas + notas[i][j][k]
contadorprofundidad = contadorprofundidad + notas[i][j][k] 
contadorarreglo = contadorarreglo + contadorprofundidad

print("promedio fila: "+ str(i+1) +"es :"+str(contadorFilas/3))
print("promedio columna: "+ str(j+1) +"es :"+str(contadorcolumnas/3))
print("promedio prfundidad: "+ str(k+1) +"es :"+str(contadorprofundidad/3))

print("promedio total: "+ str(contadorarreglo/18))