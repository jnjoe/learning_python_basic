def say_hi(name,) :
	print("Hello User") #if we simply run the proogram it will not show anything as the function has not been called
	print("Hello " + name )
	
	#functions are usually lowercase
#print("Top") will frist print this
say_hi("MIke")	
say_hi("Steve")
#print("Bottom") then it will execute say_hi function by calling from function then wiil execute Botton print



def say_hi(name, age) :
	print("Hello " + name + " , you are" +age)
	
say_hi("Mike", "35")	
say_hi("Steve","70")	



def say_hi(name, age) :
	print("Hello " + name + " , you are" + str(age))
	
say_hi("Mike", 5)	
say_hi("Steve", 7)