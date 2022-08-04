
class Ciudad():
  def __init__(self, id, distancias):
    self.id         = id
    self.distancias = distancias

    self.g         = None
    self.secuencia = []

  def __str__(self):
    print(self.id, self.distancias, end="")
    return ""

  def resetear_ciudad(self):
    self.g         = None
    self.secuencia = []