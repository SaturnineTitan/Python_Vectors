import math
# This file defines the Vector class

class Vector:
    # init() initializes objects
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # The repr() function returns the "official" string representaion of an object
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # The str() function returns an "informal" string representation of an object
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    # getitem() makes the Vector class indexable
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Out of bounds exception: Vector objects only contain 3 elements")

    # add() defines vector addition
    def __add__(self, other):
        return Vector (
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    # sub() defines vector subtraction
    def __sub__(self, other):
        return Vector (
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )


    # mul() defines vector dot product multiplication and scalar multiplication
    def __mul__(self, other):
        # vector dot product multiplication
        if isinstance(other, Vector):
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        # scalar multiplication
        elif isinstance(other, (int, float)):
            return Vector (
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("Operand must be of type Vector, int, or float.")

    # truediv() defines vector division by a scalar quantity
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector (
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("Operand must be of type int or float.")

    # The following methods implement magnitude and normalization functions

    # Return magnitude of a vector
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Return a normalized vector
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector (
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
