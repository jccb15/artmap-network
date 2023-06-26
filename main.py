import ARTMAP as am
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--entrenamiento", metavar="entrenamiento", type=int, help="cantidad de datos de entrenamiento", default=2000)
parser.add_argument("--inferencia", metavar="entrenamiento", type=int, help="cantidad de datos de entrenamiento", default=1000)
args = parser.parse_args()

red = am.RedArtmap()

#-------------Datos Ejemplos Libro------------------
#matrizLibro = [[.7, .7, 1], [.3, .8, 1], [.9, .9, 0], [.7, .9, 0], [.1, .3, 1]]
datos = am.DatosEntrenamiento()
#for dato in matrizLibro:
#    datos.ingresarDatoManual(dato[0], dato[1], dato[2])
#--------------------------------------------------

datos.generarDatosEntrenamiento(args.entrenamiento)
red.entrenar(datos.matrizDatos)

datos.limpiarDatos()
datos.generarDatosEntrenamiento(args.inferencia)

circle2 = plt.Circle((.5, .5), 0.398, color='r')
fig, ax = plt.subplots()
ax.add_artist(circle2)
plt.axis([0, 1, 0, 1])

for dato in datos.matrizDatos:
    color=red.predecir(dato[0],dato[1])
    if color== 1:
        plt.plot(dato[0], dato[1], 'bo')
    else:
        plt.plot(dato[0], dato[1], 'ko')
plt.gca().set_aspect('equal')
plt.show()