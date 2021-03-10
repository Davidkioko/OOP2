#creating a function
def my_function():
    print("Hello World")
my_function()

#function to add 2numbers
def sum (x,y):
    a=x+y
    print("The sum is",a)
sum(10,20)
sum(501,958)
#Arguments
#function to add 2numbers
def product (x,y):
    a=x*y
    print("The product is",a)
product(10,20)
product(501,958)

#function to add 2numbers
def division (x,y):
    a=x/y
    print("The division is",a)
division(10,20)
division(501,958)

#function using return
def division (x,y):
    a=x/y
    return a
print(division(10,20))
print(division(501,958))


def courses(*args):
    for subject in args:
        print(subject)
courses ("Big Data","CCNA","OOP2")

#using a return value
def courses(*args):
    for subject in args:
        return subject
print(courses ("Big Data","CCNA","OOP2","Data Comms","System Design"))

def courses(**kwargs):
    for key,value in kwargs.items():
     print("{}:{}".format(key,value))
courses(first='Big data',second='CCNA',third='HCIA')

#if we call the function without argument it uses the default value
def Kenya(County="Mombasa"):
    print("I am from " + County)
Kenya()
Kenya("Nairobi")
Kenya("Kiambu")
Kenya("Kisumu")

def student(pupil="David"):
    print("My Name is " + pupil)
Kenya()
Kenya("Max")
Kenya("Toly")
Kenya("Garry")


#Recap Passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)

def my_courses(courses):
    for x in courses:
        print(x)
courses = ["SAD","DATA COMMS","OOSAD"]
my_courses(courses)

#Area of circle
print("Area of a circle");  
def area_circle(r): 
    PI = 3.142
    return PI * (r*r); 
#prompt user
num=float(input("Enter r value:"))
print("Area is %.6f" % area_circle(num)); 









