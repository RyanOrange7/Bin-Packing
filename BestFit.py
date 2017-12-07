from Bin import Bin
from BinPacking import BinPacking

class BestFit (BinPacking):
  
  def packItems(self):
    binl = self.getBinList()
    for item in self.S:
      bestfit = binl[0]
      for bin in binl:
        if item.getWeight() <= bin.getCapacity() and  (bestfit.getCapacity() > bin.getCapacity() or bestfit.getCapacity() < item.getWeight()):
          bestfit = bin
      if bestfit.getCapacity() < item.getWeight():
        bestfit = Bin()
        binl.append(bestfit)
      bestfit.pack(item)
      item.setTrue()
      