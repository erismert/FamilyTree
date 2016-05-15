from FamilyTree import * 

def main():
	ft=FamilyTree()

	## Run Test Code ##
	test(ft)
	##
	ans=True
	while ans:
	    print ("""
	    1.Add User
	    2.Add Relation
	    3.Show Relation
	    4.Information about any person
	    5.Exit/Quit
	    """)
	    ans=raw_input("What would you like to do? ") 
	    if ans=="1":

	      print("\n Usage : Gender Name Surname Birthdate DeathDate(optional)")
	      io = map(None,raw_input().split())
	      if(len(io)>4):
	        gender,name,surname,birthdate,deathdate = io
	        print(ft.addPerson(gender,name,surname,birthdate,deathdate))
	      else:
	      	gender,name,surname,birthdate = io
	        print(ft.addPerson(gender,name,surname,birthdate))

	    elif ans=="2":

	      print("\n Usage : M/F childName M/Fname")
	      gender,childName,ParentName = map(None,raw_input().split())
	      if(gender=="Mother"):
	      	ft.setMother(childName,ParentName)
	        print(ft.setChild(childName,ParentName))
	      else:
	      	ft.setFather(childName,ParentName)
	        print(ft.setChild(childName,ParentName)) 

	    elif ans=="3":

	      print(len(ft.show()))
	      print("\n Usage : Person1 Person2")
	      person1,person2 = map(None,raw_input().split())

	      print (ft.findRelationship(person1,person2))
	    
	    elif ans=="4":
	      print("\n Usage : PersonName")
	      person = raw_input()
	      print (ft.getInformation(person))

	    elif ans=="5":

	      print("\n Goodbye")
	      ans=False 

	    elif ans !="":
	      
	      print("\n Not Valid Choice Try again") 

def test(FamilyTree):
	FamilyTree.addPerson("Male","Semih","Yildiz",1993)
	FamilyTree.addPerson("Female","Betul","Yildiz",2004)
	FamilyTree.addPerson("Male","ABaki","Yildiz",1966)
	FamilyTree.addPerson("Female","Meryem","Yildiz",1970)
	FamilyTree.addPerson("Male","Osman","Sahin",1940)
	FamilyTree.addPerson("Male","Mustafa","Yildiz",1940)
	FamilyTree.addPerson("Male","Haluk","Yildiz",1963)
	FamilyTree.setFather("ABaki","Mustafa")
	FamilyTree.setFather("Haluk","Mustafa")
	FamilyTree.setFather("Semih","ABaki")
	FamilyTree.setFather("Betul","ABaki")
	FamilyTree.setFather("Meryem","Osman")
	FamilyTree.setMother("Betul","Meryem")
	FamilyTree.setMother("Semih","Meryem")
	


if __name__ == '__main__':
	main()