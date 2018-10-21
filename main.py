import ARTMAP as am

red = am.RedArtmap()

#-------------Datos Ejemplos Libro------------------
#matrizLibro = [[.7, .7, 1], [.3, .8, 1], [.9, .9, 0], [.7, .9, 0], [.1, .3, 1]]
datos = am.DatosEntrenamiento()
#for dato in matriz:
#    datos.ingresarDatoManual(dato[0], dato[1], dato[2])
#--------------------------------------------------

datos.generarDatosEntrenamiento(1000)

red.entrenar(datos.matrizDatos)
print(red.predecir(.9, .75))
print(red.predecir(.4, .5))