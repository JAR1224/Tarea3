##########################################
#Jose Antonio Ramos
#B86485
#Tarea3
##########################################
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
from matplotlib import cm

#declarar array de datos
pmfY = [0]*21
pmfX = [0]*11
xAxis = [x for x in range(5,16)]
yAxis = [y for y in range(5,26)]

#Guardar datos en un list
with open('xy.csv', newline='') as csvfile:
  data = list(csv.reader(csvfile))

for a in range(1,12):
  for b in range(1,22):
    pmfX[a-1]+=float(data[a][b])

for a in range(1,22):
  for b in range(1,12):
    pmfY[a-1]+=float(data[b][a])

def gauss(xx, aa, bb):
  return stats.norm.pdf(xx, aa, bb)

#Encontrar las curvas de mejor ajuste para pmfX y pmfY:
param = curve_fit(gauss, yAxis, pmfY)
print('Los parametros para la pmfY son:')
print(param)

param = curve_fit(gauss, xAxis, pmfX)
print('Los parametros para la pmfX son:')
print(param)

plt.plot(yAxis, pmfY)
mu = 15.079
variance = 6.027**2
sigma = np.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.savefig('pmfY.png')
plt.clf()


plt.plot(xAxis, pmfX)
mu = 9.905
variance = 3.299**2
sigma = np.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.savefig('pmfX.png')
plt.clf()

print()
#Calculo del valor de correlacion entre x y Y:
correlacion=0.0
for x in range(1,12):
  for y in range(1,22):
    correlacion+=(x+4)*(y+4)*float(data[x][y])

print('La correlacion es:', correlacion)

#Calculo del valor de covarianza
#Primero se calcula el promedio de X y de y
#Promedio de X:
promedioX=0
for a in range(1,12):
  promedioX+=(a+4)*pmfX[a-1]
print('El promedio de X es:', promedioX)

#Promedio de Y:
promedioY=0
for a in range(1,22):
  promedioY+=(a+4)*pmfY[a-1]
print('El promedio de Y es:', promedioY)

#Covarianza
covarianza=0
for x in range(1,12):
  for y in range(1,22):
    covarianza+=((x+4)-promedioX)*((y+4)-promedioY)*float(data[x][y])

print()
print('La covarianza es:', covarianza)
print()

#Calculo del valor del coeficiente de correlacion
#Primero calculamos la desviacion estandar
#stddev de X:
stddevX=0
for a in range(1,12):
  stddevX+=((a+4)-promedioX)**2
stddevX=stddevX/11
stddevX=np.sqrt(stddevX)

print('La desviacion estandar de X es:', stddevX)

#stddev de Y:
stddevY=0
for a in range(1,22):
  stddevY+=((a+4)-promedioY)**2
stddevY=stddevY/21
stddevY=np.sqrt(stddevY)

print('La desviacion estandar de Y es:', stddevY)

#Coeficiente de correlacion
coeficiente=covarianza/(stddevX*stddevY)

print()
print('El coeficiente de correlacion es,', coeficiente)


#crear el grafico 3D
zAxis = [[0 for i in range(11)] for j in range(21)]

for x in range(1,12):
  for y in range(1,22):
    zAxis[y-1][x-1]=float(data[x][y])

zAxis = np.array(zAxis)
fig = plt.figure()
ax = fig.gca(projection='3d')
xAxis, yAxis = np.meshgrid(xAxis, yAxis)

surf = ax.plot_surface(xAxis, yAxis, zAxis, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.savefig('pmfXY.png')
plt.clf()


