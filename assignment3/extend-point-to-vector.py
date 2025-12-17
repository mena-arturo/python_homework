# -------- Task 5: Extending a Class--------------------------------------------------------------------------------
'''
1. Within the assignment3 folder, create a file called extend-point-to-vector.py.
2. Create a class called Point. It represents a point in 2d space, with x and y values passed
   to the __init__() method. It should include methods for equality, string representation,
   and Euclidian distance to another point.
3. Create a class called Vector which is a subclass of Point and uses
   the same __init__() method. Add a method in the vector class which overrides the string
   representation so Vectors print differently than Points. Override the + operator so that it implements
   vector addition, summing the x and y values and returning a new Vector.
4. Print results which demonstrate all of the classes and methods which have been implemented.
'''

'''
    def __init__(self, x, y):
        self.coordinates = (x,y)
        #self.X = x
        #self.Y = y


    def is_equal(self,x, y):
        return (self.X == x) and (self.Y == y)

    def to_string(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"

    def distance_to(self, x, y):
        return math.sqrt((x - self.X)**2 + (y - self.Y)**2)

Version2

class Point:
    
    def __init__(self, x, y):
        self.coordinates = (x,y)

    def to_string(self):
        return str(self.coordinates)

    def distance_to(self, other_point):
        # Check if other is also a Point instance
        if isinstance(other_point, Point):
            return math.sqrt((self.coordinates[0] - point.coordinates[0])**2 + (self.coordinates[1] - point.coordinates[1])**2)
        else:
            raise TypeError("Unsuported type for method distance_to: '{type(other_point).__name__}'")

    def is_equal(self,point):
        return (self.coordinates == point.coordinates)


'''

import math

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P({self.x}, {self.y})"

    def distance_to(self, other_point):
        # Check if other is also a Point instance
        if isinstance(other_point, Point):
            return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        else:
            raise TypeError("Unsuported type for method distance_to: '{type(other_point).__name__}'")

    def __eq__(self,other_point):
        if isinstance(other_point, Point):
            return (self.x == other_point.x) and (self.y == other_point.y)
        else:
            raise TypeError("Unsuported type for method ==: 'Point' and '{type(other_point).__name__}'")


class Vector(Point): #Inherits from Point
    def __init__(self, x, y):
        #Call the parent class's __init__ to set it's coordinates
        super().__init__(x, y)

    #overrides parent's str method
    def __str__(self):
        return f"V({self.x}, {self.y})"

    def __add__(self, other_vector):
        # Check if other_vector is also an instance of Vector
        if isinstance(other_vector, Vector):
            sum_x = self.x + other_vector.x
            sum_y = self.y + other_vector.y
            return Vector(sum_x, sum_y)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Vector' and '{type(other_vector).__name__}'")
    
#Testing Point class and its methods    
point1 = Point(1,1)
point2 = Point(3,4)

print("Testing Point class and its methods:\n")
print(f"Convert to string : {point1}")
print(f"Is {point1} == {point2} : {point1 == point2}")
print(f"The distance between {point1} and {point2} is {point1.distance_to(point2)}")

#Testing Vector class and its methods
print("\nTesting Vector class and its methods:\n")
vector = Vector(3,4)
vector2 = Vector(5,6)
print (f"Convert to string vector1: {vector}")
print (f"Convert to string vector2: {vector2}")
print (f"{vector} + {vector2} = {vector + vector2}")

    
        
