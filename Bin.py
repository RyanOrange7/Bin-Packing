#First Fit Implementation 
#!/usr/bin/python
import random

class Bin:

	def __init__(self):
	#Set B of items in the bin and cap is the capacity of the bin
		self.B = []
		self.cap = 100

	def getCapacity(self):
		return self.cap

	def getB(self):
		return self.B
	#packing function returns true or false to
	def pack(self, item3):
		if (self.cap - item3.getWeight()) < 0:
			print ("item cannot be packed\n")
		else:
			self.B.append(item3.getWeight())
			self.cap = self.cap - item3.getWeight()
			print(str(self.cap) + "\n")
	
	def __str__(self):
	  strp = "Items in Bin: "
	  for item5 in self.B:
	    strp = strp  + str(item5) + ", "
	  return  strp
	  
	def __repr__(self):
	  return str(self)

class Item:

  def __init__(self):
    self.weight = 0
    self.mark = False

  def getWeight(self):
    return	self.weight

  def getMark(self):
    return self.mark
    
  def setWeight(self, weight):
    self.weight = weight

  def setTrue(self):
	  self.mark = True

  def setFalse(self):
    self.mark = False

  def __repr__(self):
	  return str(self)

  def __str__(self):
	  return "item weight: " + str(self.weight)

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
      strp = strp + str(100 - bin2.getCapacity()) + ", "
    return strp

  def __repr__(self):
    return str(self)
	  