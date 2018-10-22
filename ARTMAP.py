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
        
        #ciclamos sobre cada uno de los datos de entrenamiento
        for dato in datos:
            entradaAumentada = self.calcularEntradaAumentada(dato[0], dato[1])
            
            #Si es la primera occurrencia de alguna categoria
            if dato[2] not in self.categorias:
                self.categorias.append(dato[2]) #Se agrega la categoria
                self.pesos.append(entradaAumentada) #Se asigna un nodo en pesos con el valor de la entrada aumentada
                self.valoresActivacion.append(None) #Se asigna un valor de activacion nulo para ese nodo
            
            #Si ya ha aparecido la categoria
            else:
                #Calculamos el valor de activacion para cada uno de los nodos en pesos
                for idx, peso in enumerate(self.pesos):
                    valorActivacion = self.calcularFuncionActivacion(entradaAumentada, peso)
                    self.valoresActivacion[idx] = valorActivacion
                
                #Ordenamos los valores de activacion en orden descendente
                valoresActivacionDescendente = self.valoresActivacion.copy()
                valoresActivacionDescendente.sort(reverse=True)
                
                #Bandera para saber si se ha realizado el aprendizaje
                valorEncontrado = False

                #Ciclamos sobre los valores de activacion ordenados
                for valorActivacion in valoresActivacionDescendente:
                    
                    #Obtenemos el peso correspondiente al valor de activacion mayor
                    indiceNodoGanador = self.valoresActivacion.index(valorActivacion)
                    peso = self.pesos[indiceNodoGanador]
                    
                    #Calculamos el valor de coincidentia para el valor de activacion seleccionado
                    valorCoincidencia = self.calcularFuncionCoincidencia(entradaAumentada, peso)

                    #Se realiza la prueba de vigilancia 
                    if valorCoincidencia > self.rho:

                        #Si pasa la prueba y la categoria ligada al valor de activacion corresponde a la de la entrada
                        if self.categorias[indiceNodoGanador] == dato[2]:
                            nuevoPeso = self.calcularNuevoPeso(entradaAumentada, peso) #Se calcula nuevo peso
                            self.pesos[indiceNodoGanador] = nuevoPeso #Se asigna el nuevo peso al peso del nodo seleccionado 
                            valorEncontrado = True #Activamos la bandera para indicar que se realizo el aprendizaje
                            break #salimos del ciclo
                        #Si pasa la prueba pero la categoria no coincide
                        else:
                            self.rho = valorCoincidencia + self.epsilon #Se asigna a rho el valor de coincidencia y se le suma epsilon
                            
                            #Se continua ciclando sobre el siguente valor de activacion mayor
                
                #Si ningun valor de coincidencia pasa la prueba, 
                # se genera un nuevo nodo en pesos y se asigna la entrada aumentada
                if valorEncontrado == False:
                    self.pesos.append(entradaAumentada)
                    self.categorias.append(dato[2]) #Se liga el nodo creado con la categoria que le corresponde
                    self.valoresActivacion.append(None) #Se define un valor nulo para su valor de activacion


    def predecir(self, x, y):
        entradaAumentada = self.calcularEntradaAumentada(x, y) #Se calcula la entrada aumentada
        valActivacion = []

        #Calculamos los valores de activacion para cada nodo aprendido durante el entrenamiento
        for peso in self.pesos:
            valorActivacion = self.calcularFuncionActivacion(entradaAumentada, peso)
            valActivacion.append(valorActivacion)
        
        #Regresamos la categoria correspondiente al valor de activacion mayor
        return self.categorias[valActivacion.index(max(valActivacion))]
    
    def calcularEntradaAumentada(self, x, y):
        #Calcula el complemento de los valores ingresados y regresa un arreglo de forma [x, y, x', y']
        complemento = [x, y, 1-x, 1-y]
        return complemento

    def calcularFuncionActivacion(self, entradaAumentada, pesoPrevio):
        #Calcula y regresa el valor de la funcion de activacion

        valorActivacion = Utilidades.sumatoria(Utilidades.andDifuso(entradaAumentada, pesoPrevio)) / (self.alpha + Utilidades.sumatoria(pesoPrevio))
        return valorActivacion
        
    def calcularFuncionCoincidencia(self, entradaAumentada, pesoPrevio):
        #Calcula y regresa valor de funcion de activacion (Match Function)

        valorCoincidencia = Utilidades.sumatoria(Utilidades.andDifuso(entradaAumentada, pesoPrevio)) / Utilidades.sumatoria(entradaAumentada    )
        return valorCoincidencia

    def calcularNuevoPeso(self, entradaAumentada, pesoPrevio):
        #Calcula y regresa valor de funcion para nuevo peso

        primero = [x * self.beta for x in Utilidades.andDifuso(entradaAumentada,pesoPrevio)]
        segundo = [x * (1-self.beta) for x in pesoPrevio]
        nuevoPeso = []

        for i in range(len(entradaAumentada)):
            nuevoPeso.append(primero[i] + segundo[i])
        return nuevoPeso

class DatosEntrenamiento:

    def __init__(self, radio = .398942, centroX = .5, centroY = .5):
        self.matrizDatos = np.empty((0,3), float)
        self.radio = radio
        self.centroX = centroX
        self.centroY = centroY

    def generarDatosEntrenamiento(self, cantidad = 1000):
        #Genera n pares de puntos aleatorios entre 0-1 y llama clase estaDentro
        #agrega datos generados a la matriz de datos de entranamiento
        
        for i in range(cantidad):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            
            #La matriz de datos de entrenamiento se estructura de esta forma [[dato x, dato y, etiqueta], [ , , ]]
            self.matrizDatos = np.append(self.matrizDatos,([[x, y, self.estaDentro(x,y)]]), axis=0)
        
        return self.matrizDatos

    def ingresarDatoManual(self, x, y, categoria):
        #Agrega un dato de entrenamiento a la matriz
        self.matrizDatos = np.append(self.matrizDatos,([[x, y, categoria]]), axis=0)

    def estaDentro(self, x, y):
        #Calcula la distancia entre el centro y el punto generado para determinar si el punto esta dentro o no
        distancia = math.sqrt((x - self.centroX)**2 + (y - self.centroY)**2)
        
        if distancia < self.radio:
            return 1
        else:
            return 0

    def limpiarDatos(self):
        #Limpiar datos de entrenamiento
        self.matrizDatos = np.empty((0,3), float)

class Utilidades:

    @staticmethod
    def andDifuso(arr1, arr2):
        #Cicla sobre dos arreglos, y regresa un solo arreglo con los valores minimos en cada posicion
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

    #
    @staticmethod
    def sumatoria(arr):
        #Regresa la sumatoria de los elementos de un arreglo
        suma=0
        for valor in arr:
            suma+=valor
        return suma

class Resultados:

    def imprimirResultados(self, resultados):
        print("resultados")

    def graficarResultados(self, resultados):
        print("resultados")     