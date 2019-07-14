#Object Oriented Programming Homework Assignment
#Samuel Villalva Lijo
#7/14/19

import math

print("This is my first Object Oriented Programing Homework Assignment")
print("Really helped walk me through the basics of OOP.")


print("Problem 1: Fill in the Line class methods to accept coordinatesas")
print(" a pair of tuples and return the slope and distance of the line.")

class Line:

    def __init__(self,coor1,coor2):
            
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        self.distance = math.sqrt(((self.coor2[0]-self.coor1[0])**2)+((self.coor2[1]-self.coor1[1])**2)) # use brackets [] to
        return self.distance                                                                             #accesses tuple
        
    def slope(self):
        self.slope = (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        return self.slope


coor1_g = input("Enter the 1st cordinates for the line: ").split(',')       #Remember to convert imported coordinates from
coor2_g = input("Enter the 2nd cordinates for the line: ").split(',')       #strings to integers

#use for loop to re-write coordinates from strings into integers
count_c1g = 0
for _ in coor1_g:
    coor1_g[count_c1g] = int(_)
    count_c1g += 1

count_c2g = 0
for _ in coor2_g:
    coor2_g[count_c2g] = int(_)
    count_c2g +=1


coor1_tup = tuple(coor1_g)                                                       #re-writes list coor1_g as a tuple
coor2_tup = tuple(coor2_g)  

line_1 = Line(coor1_tup,coor2_tup)

print("The distance from point 1 to point 2 is:")
print(line_1.distance())                                  

print("The slope of the line between the two points is:")
print(line_1.slope())

print("Problem 2: Create a Cylinder Object")


class Cylinder:

    pi = 3.14   #define pi as a class object attribute
    
    def __init__(self,height=1, radius=1):              #height and radius have default values of 1
        self.height = height                            # they can be written over when a new
        self.radius = radius                            # instance of the class is created
    def volume(self):
        self.volume = self.pi*(self.radius**2)*self.height
        return self.volume

    def surface_area(self):
        self.surface_area = 2*self.pi*self.radius*(self.radius+self.height) #Make sure you put an 
                                                                            #asterisk before ()
                                                                            #others you get an error
        return self.surface_area


height_c1 = float(input("Enter the height of the Cylinder: "))
radius_c1 = float(input("Enter the radius of the Cylinder: "))

cylinder_1 = Cylinder(height_c1,radius_c1)

print("The Volume of the cylinder is: ")
print(cylinder_1.volume())
print("The Surface Area of the cylinder is: ")
print(cylinder_1.surface_area())
