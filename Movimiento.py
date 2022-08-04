
import random



def imprimir_solucion(solucion):
  print(solucion[0], [i.id for i in solucion[1]])



def evaluar_solucion(solucion):
  costo = 0
  for i in range(len(solucion[1])-1):
    costo += solucion[1][i].distancias[solucion[1][i+1].id]

  if solucion[0] != costo:
    raise Exception(f"EL costo de la ruta ({solucion[0]}) es distinto al comprobado ({costo})")


  
def movimiento(solucion):
  # se escojen dos ciudades a intercambiar
  ciudad1 = random.randint(1, len(solucion[1])-2)
  ciudad2 = random.randint(1, len(solucion[1])-2)

  # si se escoje dos veces la misma ciudad se busca una distinta
  while ciudad1 == ciudad2:
    ciudad2 = random.randint(1, len(solucion[1])-2)

  #se ordenan las ciudades en orden de visita
  if ciudad1 > ciudad2:
    ciudad1, ciudad2 = ciudad2, ciudad1

  # si la ciudades se visitan consecutivamente, entoces de modifican 3 arcos
  if ciudad2 - ciudad1 == 1:
    
    # se eliminan los costos asociados a los arcos a modificar
    solucion[0] -= (solucion[1][ciudad1-1].distancias[solucion[1][ciudad1].id]
                   + solucion[1][ciudad1].distancias[solucion[1][ciudad2].id]
                   + solucion[1][ciudad2].distancias[solucion[1][ciudad2+1].id])

    #se agregan los costos de los nuevos arcos
    solucion[0] += (solucion[1][ciudad1-1].distancias[solucion[1][ciudad2].id]
                   + solucion[1][ciudad2].distancias[solucion[1][ciudad1].id]
                   + solucion[1][ciudad1].distancias[solucion[1][ciudad2+1].id])

    # se intercambia la posicion de las ciudades en la ruta
    solucion[1][ciudad1], solucion[1][ciudad2] = solucion[1][ciudad2], solucion[1][ciudad1]

  # de lo contrario se modifican 4 arcos
  else:

    # se eliminan los costos asociados a los arcos a modificar
    solucion[0] -= (solucion[1][ciudad1-1].distancias[solucion[1][ciudad1].id]
                   + solucion[1][ciudad1].distancias[solucion[1][ciudad1+1].id]
                   + solucion[1][ciudad2-1].distancias[solucion[1][ciudad2].id]
                   + solucion[1][ciudad2].distancias[solucion[1][ciudad2+1].id])

    #se agregan los costos de los nuevos arcos
    solucion[0] += (solucion[1][ciudad1-1].distancias[solucion[1][ciudad2].id]
                   + solucion[1][ciudad2].distancias[solucion[1][ciudad1+1].id]
                   + solucion[1][ciudad2-1].distancias[solucion[1][ciudad1].id]
                   + solucion[1][ciudad1].distancias[solucion[1][ciudad2+1].id])
    
    # se intercambia la posicion de las ciudades en la ruta
    solucion[1][ciudad1], solucion[1][ciudad2] = solucion[1][ciudad2], solucion[1][ciudad1]

  return solucion





