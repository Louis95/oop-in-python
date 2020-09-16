import math

class Point:
    'Represents a point in two-diamensional geometric coordinates'
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the point defaults to the origin.'''
        self.move(x, y)

    "Move the point to a new location in 2D space."
    def move(self, x, y):
        self.x = x
        self.y = y
    
    'Reset the point back to the geometric origin: 0, 0'
    def reset(self):
        self.move(0, 0)
    
    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second point passed as a parameter.
This function uses the Pythagorean Theorem to calculate the distance between the two points. The distance is
returned as a float."""
        return math.sqrt(
            (self.x - other_point.x) **2 +
            (self.y - other_point.y)
        )

point1 = Point(3,4)
point2 = Point(4,5)

point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

