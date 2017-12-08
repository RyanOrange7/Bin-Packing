from Bin import Bin
from Item import Item

class BinPacking:
  def __init__(self, S, BinList):
    #Set S of items to be packed in Set of Bins BinList
    self.S = S
    self.BinList = [Bin()]
    self.BinList = BinList
    
  def getBinList(self):
    return self.BinList
  
  def getS(self):
    return self.S
    
  
  def descending(self):
    intar = []
    for item in self.S:
      intar.append(item.getWeight())
    intar.sort(reverse = True)
    self.S = []
    for int in intar:
      item = Item()
      item.setWeight(int)
      self.S.append(item)
    
  def __str__(self):
    strp = "Weight of each bin: "
    for bin2 in self.BinList:
      strp = strp + str(10 - bin2.getCapacity()) + ", "
    return strp

  def __repr__(self):
    return str(self)
	  