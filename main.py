import ARTMAP as am

x = am.DatosEntrenamiento()
x.generarDatosEntrenamiento(10)
print(x.matrizDatos)
x.limpiarDatos()
print(x.matrizDatos)