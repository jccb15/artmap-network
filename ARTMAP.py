#Modulo para implementacion de red ARTMAP Difusa
import numpy as np
import math
import random

class RedArtmap:

    def __init__(self, rho = .5, alpha = .0000001):
        self.rho = rho
        self.alpha = alpha
        self.pesos = Pesos()

    def entrenar(self, Datos):
        print("")     

    def predecir(self, x, y):
        print("")
    
    def calcularComplemento(self, x, y):
        print("")

    def calcularValorActivacion(self, entradaAumentada):
        print("")


class Pesos:

    def __init__(self):
        self.matrizPesos = np.empty

    def actualizarPesos(self):
        print("")     


class Resultados:

    def imprimirResultados(self, resultados):
        print("resultados")

    def graficarResultados(self, resultados):
        print("resultados")            


class DatosEntrenamiento:
    #matrizDatos = np.array([1,2,3])
    def __init__(self, radio = .25, centroX = .5, centroY = .5):
        self.matrizDatos = np.zeros([1,3],dtype=float)
        self.radio = radio
        self.centroX = centroX
        self.centroY = centroY

    def generarDatosEntrenamiento(self, cantidad = 1000):
        #genera n pares de puntos aleatorios entre 0-1 y llama clase estaDentro, agrega a la matriz de datos de entranamiento
        #self.limpiarDatos()

        for i in range(cantidad):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            
            np.append(self.matrizDatos, [x , y , self.estaDentro(x,y)], 0)

    def ingresarDatoManual(self, x, y, clase):
        print("recibe dos puntos y si esta dentro o fuera y agrega a la matriz")

    def estaDentro(self, x, y):
        distancia = math.sqrt((x - self.centroX)**2 + (y - self.centroY)**2)
        
        if distancia < self.radio:
            return 1
        else:
            return 0

    def limpiarDatos(self):
        print("borrar datos de matriz")



