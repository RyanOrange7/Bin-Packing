#!/usr/bin/python
from BinPacking import BinPacking
from FirstFit import FirstFit
from NextFit import NextFit
from BestFit import BestFit
from WorstFit import WorstFit
import random
from Bin import Bin
from Item import Item


Set = []
i = 10
while i < 100:
	l = Item()
	c = random.randint(1,10)
	l.setWeight(c)
	print(l)
	Set.append(l)
	i = i + 10
print(Set)

SetFF = list(Set)
SetNF = list(Set)
SetWF = list(Set)
SetFFD = list(Set)
SetNFD = list(Set)
SetBF = list(Set)

BinFF = [Bin()]
BinNF = [Bin()]
BinWF = [Bin()]
BinFFD = [Bin()]
BinNFD = [Bin()]
BinBF = [Bin()]

FF = FirstFit(SetFF,BinFF)
FF.packItems()
print("First Fit:")
print(FF)

NF = NextFit(SetNF,BinNF)
NF.packItems()
print("Next Fit:")
print(NF)

it = Item()
it1 = Item()
it2 = Item()
it3 = Item()
it4 = Item()
it5 = Item()
it6 = Item()

it.setWeight(95)
it1.setWeight(6)
it2.setWeight(3)
it3.setWeight(4)
it4.setWeight(2)
it5.setWeight(2)
it6.setWeight(2)
stemp = [it,it1,it2,it3,it4,it5,it6]

WF = WorstFit(SetWF,BinWF)
WF.packItems()
print("Worst Fit:")
print(WF)

FFD = FirstFit(SetFFD,BinFFD)
FFD.FFdescending()
print("First Fit Descending:")
print(FFD)

NFD = NextFit(SetNFD,BinNFD)
NFD.NFdescending()
print("Next Fit Descending:")
print(NFD)

it.setWeight(95)
it1.setWeight(8)
it2.setWeight(5)
it3.setWeight(93)
it4.setWeight(7)
it5.setWeight(93)
it6.setWeight(7)
stemp = [it,it1,it2,it3,it4,it5,it6]
BF = BestFit(SetBF,BinBF)
BF.packItems()
print("Best Fit:")
print(BF)
