#!/usr/bin/python
from Bin import Bin
from BinPacking import BinPacking

class NextFit (BinPacking):
  def packItems(self):
    binl = self.getBinList()
    bin = binl[0]
    for item in self.S:
      if item.getWeight() <= bin.getCapacity():
        bin.pack(item)
      else:
        newBin = Bin()
        binl.append(newBin)
        bin = newBin
        bin.pack(item)

  def writeOutputFile(self,string):      
    file = open(string,"w")
    file.write("Next Fit Bin Packing:\n")

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

        
  def NFdescending(self):
	  self.descending()
	  print(self.S)
	  self.packItems()