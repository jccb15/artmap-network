#Modulo para implementacion de red ARTMAP Difusa
import numpy as np
import math
import random

class RedArtmap:

    def __init__(self, rho = .5, alpha = .0000001, beta = 1, epsilon = .001 ):
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon
        self.pesos = []
        self.categorias = []

    def entrenar(self, datos):
        print("")


    def predecir(self, x, y):
        print("")
    
    def calcularEntradaAumentada(self, x, y):
        complemento = [x, y, 1-x, 1-y]
        return complemento

    def calcularFuncionActivacion(self, entradaAumentada, nodo):
        print("")

    def calcularMatchFunction(self, entradaAumentada, nodo):
        print("")
    

class Resultados:

    def imprimirResultados(self, resultados):
        print("resultados")

    def graficarResultados(self, resultados):
        print("resultados")            


class DatosEntrenamiento:

    def __init__(self, radio = .25, centroX = .5, centroY = .5):
        self.matrizDatos = np.empty((0,3), float)
        self.radio = radio
        self.centroX = centroX
        self.centroY = centroY

    def generarDatosEntrenamiento(self, cantidad = 1000):
        #genera n pares de puntos aleatorios entre 0-1 y llama clase estaDentro, agrega a la matriz de datos de entranamiento
        self.limpiarDatos()

        for i in range(cantidad):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            
            #La matriz de datos de entrenamiento se estructura de esta forma [[dato x, dato y, etiqueta], [ , , ]]
            self.matrizDatos = np.append(self.matrizDatos,([[x, y, self.estaDentro(x,y)]]), axis=0)

    def ingresarDatoManual(self, x, y, categoria):
        self.matrizDatos = np.append(self.matrizDatos,([[x, y, categoria]]), axis=0)

    def estaDentro(self, x, y):
        distancia = math.sqrt((x - self.centroX)**2 + (y - self.centroY)**2)
        
        if distancia < self.radio:
            return 1
        else:
            return 0

    def limpiarDatos(self):
        #borrar datos de matriz
        self.matrizDatos = np.empty((0,3), float)



