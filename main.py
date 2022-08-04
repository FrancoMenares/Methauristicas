
import Generador as generador
import Lectura as lectura
import Memoria as memoria

import Branch_and_Bound
import Greedy
import Hill_Climbing
import Tabu_Search



num_instancia = 1
semilla       = 0
ciudades      = 100

generador.generar_instancia(num_instancia, semilla, ciudades)
instancia = lectura.leer_instancia(num_instancia)

"""
print()
print(instancia[0])
for i in instancia[1]:
  print(i)
print()
"""


resultados = []   # metodologia, tiempo CPU, costo, ruta

#resultados.append(Branch_and_Bound.resolver(instancia))

#"""
resultados.append(Greedy.resolver(instancia))

iteraciones = 1000
detencion   = 50
reinicios   = 0
resultados.append(Hill_Climbing.resolver(instancia, iteraciones, detencion, reinicios))

iteraciones = 1000
reinicios   = 50
resultados.append(Hill_Climbing.resolver(instancia, iteraciones, detencion, reinicios))
#"""

for i in resultados:
  #print(i)
  print(i[0], i[1], i[2])

#print(f"{ciudades} {resultados[0][1]} {round(memoria.memory_usage_psutil(),5)}")