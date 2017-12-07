#!/usr/bin/python
from Bin import Bin
from BinPacking import BinPacking


class FirstFit (BinPacking):
	
	def packItems(self):
		for item1 in self.S:
		 for bin2 in self.BinList:
				if item1.getWeight() <= bin2.getCapacity() :
					bin2.pack(item1)
					item1.setTrue()
		 if item1.getMark() == False:
				newbin = Bin()
				self.BinList.append(newbin)
				newbin.pack(item1)
	
	def FFdescending(self):
	  self.descending()
	  print(self.S)
	  self.packItems()
