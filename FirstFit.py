#!/usr/bin/python
from Bin import Bin
from BinPacking import BinPacking


class FirstFit (BinPacking):
	
	def packItems(self):
		for item in self.S:
		 for bin in self.BinList:
			if item.getWeight() <= bin.getCapacity() :
				bin.pack(item)
				item.setTrue()
				break
		 if item.getMark() == False:
			newbin = Bin()
			self.BinList.append(newbin)
			newbin.pack(item)
			item.setTrue()
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
