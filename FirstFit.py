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
		self.writeOutputFile()

	def writeOutputFile(self):			
		file = open("FFoutput.txt","w")
		file.write("First Fit Bin Packing:\n")

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
		
	def FFdescending(self):
	  self.descending()
	  print(self.S)
	  self.packItems()
