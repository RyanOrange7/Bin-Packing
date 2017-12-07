#!/usr/bin/python
from Bin import Bin
from BinPacking import BinPacking

class NextFit (BinPacking):
  def packItems(self):
    binl = self.getBinList()
    counter = 0
    bin = binl[counter]
    for item in self.S:
      if item.getWeight() <= bin.getCapacity():
        bin.pack(item)
        item.setTrue()
      else:
        newbin = Bin()
        binl.append(newbin)
        counter = counter + 1
        bin = binl[counter]
        bin.pack(item)
        item.setTrue()
        
  def NFdescending(self):
	  self.descending()
	  print(self.S)
	  self.packItems()