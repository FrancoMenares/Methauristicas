
from math import inf
import copy
import time

import Solucion_Inicial
import Movimiento



def imprimir_solucion(solucion):
  print(solucion[0], [i.id for i in solucion[1]])



def resolver(instancia, iteraciones, detencion, reinicios):
  inicio = time.time()

  # se guarda mejor costo y mejor solucion
  mejor_costo    = inf
  mejor_solucion = None

  #se itera en la cantidad de reinicios (una iteracion si no hay reinicios)
  for i in range(reinicios+1):

    solucion  = Solucion_Inicial.solucion_aleatoria(instancia) # se crea una solucion inicial
    #solucion  = Solucion_Inicial.solucion_greedy(instancia)    # se crea una solucion inicial
    estancado = 0                                              # se setea la cantidad de iteraciones estancadas

    # si la solucion generada es mejor que la mejor solucion conocida, se actualiza la mejor solucion conocida
    if solucion[0] < mejor_costo:
      mejor_costo = solucion[0]
      mejor_solucion = copy.deepcopy(solucion)

    #se recorren las iteraciones del algoritmo
    for i in range(iteraciones):
  
      solucion = Movimiento.movimiento(solucion)  # se explora una solucion vecina
    
      # si la solucion generada es mejor que la mejor solucion conocida, se actualiza la mejor solucion conocida
      if solucion[0] < mejor_costo:
        mejor_costo = solucion[0]
        mejor_solucion = copy.deepcopy(solucion)
        estancado = 0
      # si no se encuentra una mejor solucion se incrementa la cantidad de iteraciones estancadas 
      else:
        estancado += 1

        # si se cumple el criterio de estancamiento se reinicia el algoritmo
        if estancado == detencion:
          break


  tiempo = round(time.time() - inicio, 5)

  return ["Hill Climbing (" + str(reinicios) +")", tiempo, mejor_solucion[0], [i.id for i in mejor_solucion[1]]] 




