
from math import inf
import time



def evaluar_solucion(solucion):
  costo = 0
  for i in range(len(solucion[1])-1):
    costo += solucion[1][i].distancias[solucion[1][i+1].id]

  if solucion[0] != costo:
    raise Exception(f"EL costo de la ruta ({solucion[0]}) es distinto al comprobado ({costo})")



def resolver(instancia):
  inicio = time.time()

  origen   = instancia[0]                      # ciudad de origen
  ciudades = instancia[1]                      # ciudades del problema
  ciudades_id = [i.id for i in instancia[1]]   # id de las ciudades
  
  costo = 0            # costo de la ruta
  ruta  = [origen.id]  # ruta

  # mientras no se visiten todas las ciudades
  while len(ruta) < len(ciudades):
    
    siguientes_ciudades = list(set(ciudades_id).difference(set(ruta)))  # ciudades que aun no han sido visitadas
    min_ciudad          = None                                          # ciudad mas cercana
    min_costo           = inf                                           # costo a la ciudad mas cercana
    
    # se recorren las ciudades qu aun no han sido visitadas
    for i in siguientes_ciudades:

      # si se encuentra una ciudad mas cercana
      if ciudades[ruta[len(ruta)-1]].distancias[i] < min_costo:
        min_costo  = ciudades[ruta[len(ruta)-1]].distancias[i]  # se actualiza el costo a la ciudad mas cercana
        min_ciudad = i                                          # se actualiza la ciudad mas cercana

    costo += min_costo        # se actualiza el costo de la ruta
    ruta.append(min_ciudad)   # se agrega la ciudad mas cercana la ruta

  costo += ciudades[ruta[len(ruta)-1]].distancias[origen.id]  # se agrega el costo de retornar al origen
  ruta.append(origen.id)                                      # se agrega el origen a la ruta

  tiempo = round(time.time() - inicio, 5)

  return ["Greedy", tiempo, costo, ruta] 
