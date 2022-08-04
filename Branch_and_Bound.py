
from math import inf
import copy
import queue
import time



def resolver(instancia):
  inicio = time.time()
  
  expansiones = 0     # numero de ramas que se exploradas
  podas       = 0     # numero de ramas padadas
  mejor_ruta  = []    # mejor(s) ruta(s) encontrada(s)
  mejor_costo = inf   # mejor costo encontrado

  cola        = queue.LifoQueue()  # cola lifo: ultimo en entrar primero en salir

  origen   = instancia[0]                      # ciudad de origen
  ciudades = instancia[1]                      # ciudades del problema
  ciudades_id = [i.id for i in instancia[1]]   # id de las ciudades

  # se agrega el origen a la cola
  actual_ciudad           = origen
  actual_ciudad.g         = 0
  actual_ciudad.secuencia = [actual_ciudad.id]
  cola.put(actual_ciudad)

  # mientras queden ciudades en la cola se sigue explorando
  while cola.qsize() > 0:

    actual_ciudad = cola.get()  # se saca la ultima ciudad de la cola

    # si todas las ciudades estan en la ruta
    if len(actual_ciudad.secuencia) == len(ciudades):

      # si se encuentra una mejor ruta, se actualiza el mejor costo y la mejor ruta guardada
      if actual_ciudad.g < mejor_costo:
        mejor_costo = actual_ciudad.g
        mejor_ruta  = copy.deepcopy(actual_ciudad.secuencia) + [origen.id]
        continue

      # si se encuentra una ruta tan buena como la mejor encontrada, tambien se guarda
      #if actual_ciudad.g == mejor_costo:
      #  mejor_ruta.append(copy.deepcopy(actual_ciudad.secuencia) + [origen.id])
      #  continue

    # ciudades que aun no han sido visitadas
    siguientes_ciudades = list(set(ciudades_id).difference(set(actual_ciudad.secuencia))) 

    # si quedan ciudades por visitar
    if len(siguientes_ciudades) > 0:

      # se avaluan las ciudades faltantes
      for i in siguientes_ciudades:
        siguiente_ciudad = copy.deepcopy(ciudades[i]) #ciudad a evaluar

        # si es la ultima ciudad a visitar, entonces se activa bandera para retornar al deposito
        if len(actual_ciudad.secuencia)+1 == len(ciudades):
          bandera = 1
        else:
          bandera = 0
  
        # si el costo a la siguiente ciudad es menor que el mejor costo encontrado se expande la rama
        if actual_ciudad.g + actual_ciudad.distancias[i] + siguiente_ciudad.distancias[origen.id]*bandera < mejor_costo:
          expansiones                += 1
          siguiente_ciudad.g         = actual_ciudad.g + actual_ciudad.distancias[i] + siguiente_ciudad.distancias[origen.id]*bandera
          siguiente_ciudad.secuencia = copy.deepcopy(actual_ciudad.secuencia)
          siguiente_ciudad.secuencia.append(siguiente_ciudad.id)
          cola.put(siguiente_ciudad)
          
        # si el costo a la siguiente ciudad es mayor que el mejor costo encontrado se poda la rama
        else:
          podas += 1

  tiempo = round(time.time() - inicio, 5)

  return ["Branch and Bound", tiempo, mejor_costo, mejor_ruta] #, expansiones, podas












