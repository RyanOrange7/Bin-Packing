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

      
  def writeOutputFile(self, string):      
    file = open(string,"w")
    file.write("Best Fit Bin Packing:\n")

    count = 0
    binl = self.getBinList()
    for bin in binl:
      s = "B" + str(count) + " = [ "
      file.write(s)
      for item in bin.getB():
        s = str(item) +", " 
        file.write(s)
      file.write("]\n")
      count = count + 1
    file.close()
