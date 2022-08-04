
import Ciudad



def leer_instancia(instancia):
  ciudades = []
  origen   = None
  with open("Instancia" + str(instancia) + ".txt", "r") as archivo:
    i = 0
    for linea in archivo:
      x = linea.split()
      x = [int(j) for j in x]
      if i == 0:
        origen = x[0]
      else:
        ciudad = Ciudad.Ciudad(i-1, x)
        if origen == ciudad.id:
          origen = ciudad
        ciudades.append(ciudad)
      i += 1
  return [origen, ciudades]








