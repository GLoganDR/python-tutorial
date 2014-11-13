# This is a comment

#importing math

import math

# for just pi use from math import pi

# All statements don't use semi-colons to close lines. 

# There is no var. You just say x = 3

x = 3 #integer
y = 4.2 #floating point number
z = 'hello'
a = "world"
b = x + y - x
c = 8 / 3
d = 8 //3 # Discards the fractional part
e = 8 % 3 #modulus
f = 8 ** 3 #does powers
g = z + a

# print = console.log

print(x, y, z, a, b, c, d, e, f, g)

# if statement

age = 20
gender = 'female'

if age >= 21 and (gender == 'female' or gender == male):
  print('go have a drink')
else:
  print('go have your parents buy you a drink')

# ranges

for x in range(20, -50, -5):
  print("{0} to the {1} power is {2}".format(x, 2, x**2))

# make an array of tuples where the first number is even and the second number is its square using ranges to span 0-20

evens = [(x, x**2, y**3, x*y) for x in range(0, 20, 2) for y in range(3, 15, 3) if x == 10]

# functions should do one thing and one thing only. Single Responsibility Principle.

# WRITING FUNCTIONS

def sum(a, b):
    return a + b

a = sum(3,4)

#pi = 3.14159
#radius = 2
#height = 10
#base_area = pi * radius ** 2
#volume = base_area * height
#surface_area = 2 * base_area + 2 * pi * radius * height
#print "volume is", volume, ", surface area is", surface_area

math.pi
print math.pi

def vol(height, radius):
    return height * math.pi * (radius ** 2)

b = vol(5,6)

print a,b

def bin2dec(bin):
    sum = 0
    for index, bit in enumerate(bin[::-1]):
        sum += int(bit) * (2**index)
    return sum

dec = bin2dec('10001')
print dec


a = 4