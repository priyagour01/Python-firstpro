# Indentifier is a name that can be used to identifier object.
# It can be (variable name, function name, class_name , module , package, library) 

# Rules for Indentifier.
# 1) dose not start with digit.
#x = 10
#print(x)

#5 = 18
#print(5)
#xyz = 20
#print(xyz)
#1xyz = 30
#print(1xyz)

# 2) start with _a-z or _A-Z or _underscore.
xYz = 10
print(xYz)

Xyz = 20
print(Xyz)

xyZ = 30
print(xyZ)

_x = 40
print(_x)

_xyz = 50
print(_xyz)

#3) case sensitive.
x = 5
print(x)
print(type(x))

#4) combination of alphabates and _underscore.
_123xyz = 30
x_123 = 40
x12_3 = 60
print(x_123)
print(x12_3)
print(_123xyz)


 # priya name ki jagah yahan pr number bhi rakh sakte hai.
x_y = "priya"
priya_gour = "priya"
print(priya_gour)

name = "Priya gour"
age = 23
cource = "Python"
print("My name is" , name)
print("My age is" , age)
print("My cource is" , cource)

name = "Priya gour"
age =  23
cource = "Python"
print(id(name))
print(id(age))
print(id(cource))

# 5) Literals Type: 
#1) Numeric Literals : int , float , complex , string , list , tuple , dictonary ye sabhi sequential collection hota h 
#inhe hum orderd collection bhi kehte hai.

# 1) Integer : 
x= 10
print(x)
print(type(x))

# Float :
a = 10.5
print(a)
print(type(a))

# Complex : 
#y = 10 + 10j
y = 10 +5j
print(y)
print(type(y))

# 2) String :
# srting is a collection or charractors.
# represent in double or single  or tripple quote '_' , "_" , '''_''' .  single or double single line ke liye use kiya jata h.

# Single line 
# x = 'Python'
# print(x)
# y = "JavaScript"
# print(y)
# z = '''C++'''
# print(z)
# print(x,y,z)

# Multi line 
#x ='Python
#Language'
#print(x)

#y = "Python
#Language"
#print(y)

#z = '''Python 
#Language'''
#print(z)

m = 'This is "Python" class'
print(m)

# List : Collection of homogenous data as well as hetrogenous data element.
# 1) Homogenous : collection of same data types.
# 2) Hetrogenous : collection of different data types.
# Homogenous and Hetrogenous represent in [] with comma (,) separated elements.

l = [12,23,45,'Python', 10.6, 'javascript' ,['HTML' , 'css']] 
print(l)
print(type(l))

l1 = [1,2,3,4,5,6,7,8,9,90]
print(l1)
print(type(l1))

l2 = ["Python" , 'JavaScript' , 'c++']
print(l2)
print(type(l2))

# Dictonary : collection of 'key' : 'value' pairs 
# represent in {} with comma(,)  seperated elements.
# Example : 
d = {'name' : "Priya" , 'age' : 23 , 'cource' : 'Python'}
print(d)
print(type(d))

# Set and Frozenset : {unorderd collection} collection of unique elements.
# Set : collection of unique elements homogenous or hetrogenous.
# represent in {} with comma(,) separeted elements.

s1 = {10,20,30,30 ,'python' , 10.3 , 'java' , 'javascript' , 'java'} 
print(s1)
print(type(s1))

# Frozenset :collection of unique elements homogenous or hetrogenous.
# it used to freeze any collection with comma(,) separeted elements or isko hashing technique se freeze kiya jata h.

s2 = {10,20,30,30, 'python' , 5.5 , 'mern' , 'node' , 'mern' , 'java'}
x =frozenset(s2)
print(x)
print(type(x))

x = "Python"
x = frozenset(x)
print(x)
print(type(x))

# Python Inbuild Functions :
print()
type()
input()
max()
min()
length()
sum()

# Python Inbuild Class :
int
str
float -> set
complex -> frozenset
bool
list
tuple
dict




