#python program to show that variables with a 
#value assigned in class declaration , are class
#variables and variables inside methods and
#constructors areinstance variables
#class for computer science student

class CSStudent:
	
    #class variable
	stream= 'cse'
	
	#the init method or constructor
	def_init_(self,roll):
	#instance variable
	self.roll=roll:
#objects of csstudent class
a=CSStudent(101)
b=CSStudent(102)

print(a.stream)#prints "cse"
print(b.stream)#prints "cse"
print(a.roll)#prints 101
#class variable can be accessed using class
#name also
print (CSStudent.stream)#prints "cse"