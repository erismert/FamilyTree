from Person import *

class FamilyTree(object):

    def __init__(self):
        self.familyTree = []

    def addPerson(self,gender,name,surname,birthdate,deathdate=""):
        self.familyTree.append(Person(gender,name,surname,birthdate,deathdate))


    def setChild(self,childName,personName):
        child = self.getPerson(childName)
        person= self.getPerson(personName)
        if not child or not person:
          return "No found child or person"
        if(self.isDie(person)):
          if(int(person.deathdate)<int(child.birthdate)):
          	return "This condition does not come true"
        if(2016-int(person.birthdate)<18):
          return "Person can not be have child because of age"
        person.children.append(child)
        return "Set child"

    def setMother(self,childName,motherName):
        child = self.getPerson(childName)
        mother= self.getPerson(motherName)
        if not child or not mother:
          return "No found child or mother"
        child.mother = mother
        mother.children.append(child)
        return "Set mother"

    def setFather(self,childName,fatherName):
        child = self.getPerson(childName)
        father= self.getPerson(fatherName)
        if not child or not father:
          return "No found child or father"

        child.father = father
        father.children.append(child)
        return "Set father"


    def getPerson(self,personName):
        for anyPerson in self.familyTree:
          if anyPerson.name==personName:
            return anyPerson

    def getInformation(self,personName):
        person = self.getPerson(personName)
        if(not person.deathdate):
          age=2016-int(person.birthdate)
          return "aLive Age %d Level: " % age
        else:
          age=int(person.deathdate)-int(person.birthdate) 
          return "dead Age %d Level: " % age

    def isDie(self,person):
    	if(person.deathdate):
    	  return True
    	else:
    	  return False

    def show(self):
    	return self.familyTree

    def findParentalRelation(self,person,target,generations):
        if self.traverse_down_tree(person, target, generations):
            if person.gender == 'Male':
                return self.add_greats(generations[0], 'Father')
            elif person.gender == 'Female':
                return self.add_greats(generations[0], 'Mother')
            else:
                return self.add_greats(generations[0], 'Parent')            
        elif self.traverse_down_tree(target, person, generations):
            if person.gender == 'Male':
                return self.add_greats(generations[0], 'Son')
            elif person.gender == 'Female':
                return self.add_greats(generations[0], 'Daughter')
            else:
                return self.add_greats(generations[0], 'Child')
        else:
            return ''

    def add_greats(self, generations, relation):
	    if generations == 1:
	        return relation

	    relation = 'Grand ' + relation
	    
	    #Grandparent is generations = 2 so skip adding greats
	    while generations > 2:
	        relation = 'Great ' + relation
	        generations = generations - 1

	    return relation

    def traverse_down_tree(self, person, target, generations):
	    if person.name == target.name:
	        return True
	    
	    currentGenerations = generations[0]

	    for child in person.children:
	        generations[0] += 1
	        if not self.traverse_down_tree(child, target, generations):
	            generations[0] = currentGenerations
	        else:
	            return True
	    return False

    def findSibling(self,p1,p2):

        if p1.father==p2.father or p1.mother==p2.mother:
          if p1.gender=="Male":
      		if p1.birthdate>p2.birthdate:
      			return "Erkek Kardes"
      		else:
      			return "Abi"
          if p1.gender=="Female":
      		if p1.birthdate>p2.birthdate:
      			return "Kiz Kardes"
      		else:
      			return "Abla"
        else:
          return ""	

    def findUncle_Aunt(self,p1,p2):
    	if p2.father.father==p1.father:
    	  if p1.gender=="Male":
    	  	return "Amca"
    	  if p2.gender=="Female":
    	  	return "Hala"
    	elif p1.father.father==p2.father:
    	  return "Yegen"
    	elif p2.mother.father==p1.father:
    	  if p1.gender=="Male":
    	  	return "Dayi"
    	  if p2.gender=="Female":
    	  	return "Teyze"
    	elif p1.mother.father==p2.father:
    	  return "Yegen"
    	else:
    	  return ""

    def findRelationship(self,person1,person2):
    	p1 = self.getPerson(person1)
        p2 = self.getPerson(person2)
        
        if not p1 or not p2:
          return 'Name not found'

        generations = [0,0]

        relation = self.findParentalRelation(p1, p2, generations)
        if relation:
          return relation

        relation = self.findSibling(p1,p2)
        if relation:
          return relation
        
        relation = self.findUncle_Aunt(p1,p2)
        if relation:
		  return relation

