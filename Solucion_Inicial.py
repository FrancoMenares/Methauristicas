
import random

import Greedy



def solucion_greedy(instancia):
  solucion = Greedy.resolver(instancia)           # se crea solucion greedy
  
  for i in range(len(solucion[3])):
    solucion[3][i] = instancia[1][solucion[3][i]] # se convierte de ruta id a ruta ciudades
  
  return [solucion[2], solucion[3]]



def solucion_aleatoria(instancia):
  ciudades_id = [i.id for i in instancia[1]]   # id de las ciudades
  costo = 0                                    # costo de la ruta
  ruta = [instancia[0].id]                     # secuencia de ciudades, comienza en el origen

  # mientras la ruta no este completa
  while len(ruta) < len(ciudades_id):
    siguientes_ciudades = list(set(ciudades_id).difference(set(ruta)))     # se obtienen ciudades faltantes en la ruta
    siguiente_ciudad = random.choice(siguientes_ciudades)                  # se escoge aleatoriamente una ciudad faltante
    costo += instancia[1][ruta[len(ruta)-1]].distancias[siguiente_ciudad]  # se suma el cos a la ciudad
    ruta.append(siguiente_ciudad)                                          # se agrega la ciuda a la ruta
  costo += instancia[1][ruta[len(ruta)-1]].distancias[instancia[0].id]     # se suma el costo de volver al origen
  ruta.append(instancia[0].id)                                             # se agrega el origen a la ruta
  
  for i in range(len(ruta)):
    ruta[i] = instancia[1][ruta[i]]  # se convierte de ruta id a ruta ciudades
  
  return [costo, ruta]














