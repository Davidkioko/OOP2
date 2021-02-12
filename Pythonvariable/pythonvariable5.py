#this function modifies global variable 's'
def f():
	global s
	print (s)
	s="Look for Geeks for geeks python section"
	print(s)
#global scope
s="Python is great!"
f()
print(s)
