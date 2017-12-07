from Bin import Bin
from BinPacking import BinPacking

class WorstFit (BinPacking):
  
  def packItems(self):
    binl = self.getBinList()
    for item in self.S:
      worstfit = binl[0]
      for bin in binl:
        if item.getWeight() <= bin.getCapacity() and ( worstfit.getCapacity() < bin.getCapacity() or worstfit.getCapacity() < item.getWeight()):
          worstfit = bin
        if worstfit.getCapacity() < item.getWeight():
          worstfit = Bin()
          binl.append(worstfit)
      worstfit.pack(item)
      item.setTrue()
      