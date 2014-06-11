# -*- coding: utf-8 -*-
class Animal:
	"This is a class representing different attributes of different animals"

	def __init__(self,numberOfLegs,color,presenceOfFur,weight,length,species,name):
		self.numberOfLegs = numberOfLegs
		self.color = color
		self.presenceOfFur = presenceOfFur
		self.weight = weight
		self.length = length
		self.species = species
		self.name = name

	def getName(self):
		return self.name
	def getSpecies(self):
		return self.species
	def __str__(self):
		return "%s is a %s" % (self.name, self.species)

	def sleep(self):
		print self.name , " the " , self.species, " is sleeping."
 
	def breathe(self):
		print self.name , " the " , self.species, " is breathing."
	
	def walk(self):
 		print self.name , " the " , self.species, " is walking."


Dog = Animal(4, "brown", "true",  24,  36, "canine", "Roofus")
Cat = Animal(4, "grey", "true",  7,  27, "feline",  "Mischief")

Dog.sleep()
Dog.breathe()
Dog.walk()

Cat.sleep()
Cat.breathe()
Cat.walk()

print Dog.__str__()
print Cat.__str__()

