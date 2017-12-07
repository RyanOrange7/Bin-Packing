class Item:

  def __init__(self):
    self.weight = 0
    self.mark = False

  def getWeight(self):
    return	self.weight

  def getMark(self):
    return self.mark
    
  def setWeight(self, weight):
    self.weight = weight

  def setTrue(self):
	  self.mark = True

  def setFalse(self):
    self.mark = False

  def __repr__(self):
	  return str(self)

  def __str__(self):
	  return "item weight: " + str(self.weight)