
import random 



def generar_instancia(instancia, semilla, cant_ciudades):
  random.seed(semilla)
  origen = random.choice([i for i in range(cant_ciudades)])
  distancias = [[random.randint(20, 50) if j != i else 0 for j in range(cant_ciudades)] for i in range(cant_ciudades)]

  with open("Instancia" +str(instancia) + ".txt", 'w') as archivo:
    archivo.write(str(origen) + "\n")
    for i in distancias:
      for j in i:
        archivo.write(str(j) + "\t")
      archivo.write("\n")

  








