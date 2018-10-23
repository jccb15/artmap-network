import ARTMAP as am
from matplotlib import pyplot as plt

red = am.RedArtmap()

#-------------Datos Ejemplos Libro------------------
#matrizLibro = [[.7, .7, 1], [.3, .8, 1], [.9, .9, 0], [.7, .9, 0], [.1, .3, 1]]
datos = am.DatosEntrenamiento()
#for dato in matrizLibro:
#    datos.ingresarDatoManual(dato[0], dato[1], dato[2])
#--------------------------------------------------

datos.generarDatosEntrenamiento(50)
red.entrenar(datos.matrizDatos)

datos.limpiarDatos
datos.generarDatosEntrenamiento()

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

plt.show()