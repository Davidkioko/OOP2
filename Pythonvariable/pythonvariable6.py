a=1
#uses global because there is no local 'a'
def f():
	print(	'inside f():',a)
#variable 'a' is refined as a local
def g ():
	a=2
	print('Inside g():',a)
#uses global keyword to modify global 'a'
def h():
	global a
	a=3
	print('Inside h()=',a)
#Global scope
print ('global:',a)