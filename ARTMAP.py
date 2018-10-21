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
        self.valoresActivacion = []

    def entrenar(self, datos):
        for dato in datos:
            print (dato)
            entradaAumentada = self.calcularEntradaAumentada(dato[0], dato[1])
            
            if dato[2] not in self.categorias:
                self.categorias.append(dato[2])
                self.pesos.append(entradaAumentada) 
                self.valoresActivacion.append(None)
            
            else:
                for idx, peso in enumerate(self.pesos):
                    valorActivacion = self.calcularFuncionActivacion(entradaAumentada, peso)
                    self.valoresActivacion[idx] = valorActivacion
                
                indiceNodoGanador = self.valoresActivacion.index(max(self.valoresActivacion))
                peso = self.pesos[indiceNodoGanador]

                if self.categorias[indiceNodoGanador] == dato[2]:
                    

                valorCoincidencia = self.calcularFuncionCoincidencia(entradaAumentada, peso)
                if valorCoincidencia >= self.rho:
                    nuevoPeso = self.calcularNuevoPeso(entradaAumentada, self.pesos[self.categorias.index(dato[2])])
                    self.pesos[self.categorias.index(dato[2])] = nuevoPeso

                    

    def predecir(self, x, y):
        print("")
    
    def calcularEntradaAumentada(self, x, y):
        complemento = [x, y, 1-x, 1-y]
        return complemento

    def calcularFuncionActivacion(self, entradaAumentada, pesoPrevio):
        valorActivacion = Utilidades.sumatoria(Utilidades.andDifuso(entradaAumentada, pesoPrevio)) / (self.alpha + Utilidades.sumatoria(pesoPrevio))
        return valorActivacion
        
    def calcularFuncionCoincidencia(self, entradaAumentada, pesoPrevio):
        valorCoincidencia = Utilidades.sumatoria(Utilidades.andDifuso(entradaAumentada, pesoPrevio)) / Utilidades.sumatoria(entradaAumentada    )
        return valorCoincidencia

    def calcularNuevoPeso(self, entradaAumentada, pesoPrevio):
        primero = [x * self.beta for x in entradaAumentada]
        segundo = [x * (1-self.beta) for x in pesoPrevio]

        nuevoPeso = []
        for i in range(len(entradaAumentada)):
            nuevoPeso.append(primero[i] + segundo[i])
        return nuevoPeso

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
        
        return self.matrizDatos

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

class Utilidades:

    @staticmethod
    def andDifuso(arr1, arr2):
        resultado = []
        if len(arr1) == len(arr2):
            for i in range(len(arr1)):
                if arr1[i] > arr2[i]:
                    resultado.append(arr2[i])
                else:
                    resultado.append(arr1[i])
            return resultado
        else:
            print("andDifuso: los arreglos no son del mismo tamaño")

    @staticmethod
    def sumatoria(arr):
        suma=0
        for valor in arr:
            suma+=valor
        return suma

