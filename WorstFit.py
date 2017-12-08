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

      
  def writeOutputFile(self, string):      
    file = open(string,"w")
    file.write("Worst Fit Bin Packing:\n")

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
