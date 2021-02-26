#Python strings
a="Banana"
b="Orange"
print(a<b)
print(b>a)
print(a<=b)
print(a>=b)
print(a+b)
print(a*3)
print('anne\'s daughter')
print("Man's property")
print('''Anne's man''')
a="5"
b="10"
print(a+b)
print(b+a)
q="Max"
letter=q[-1]
print(letter)
s="banana"
print(s[1:5])
print(s[:])
print(s[:5])
print(s[::3])
print(s[-5:-2])


s1="Anne"
s2="Max"
s3=""
print(len(s1),   end=" ")
print(len(s2) , end=" ")
print(len(s3))

x=30
y=40
print("The sum of %d and %d is %d" % (x, y, x+ y))


x=23.0
y=21.5
print("The sum of %f and %f is %f" % (x , y ,x + y))

x="My"
y="Dior"
print("The sum of %s and %s is %s" % (x, y, x + y))

x="hello world"
print(len(x))
print(x.upper())
print(x.lower())
print(x.replace('h','y'))
print(x.swapcase())
print(x.join(x))
print(x.isnumeric())
print(x.isalpha())
print(x.isalnum())