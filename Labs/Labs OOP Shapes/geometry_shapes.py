from __future__ import annotations
from dataclasses import dataclass
import math

#TODO finish before deadline

"""
Class should have:

area property (Done for rectangle)
circumference property

operator overload av == för att checka likhet

operator overload av komparatoroperatorer <,>,<=>,> för jämförelser
override av __repr__()
override av __str__

x och y som representerar mittpositionen av objektet
en translationsmetod som gör det möjligt att förflytta x och y
en metod som checkar om en viss punkt befinner sig innanför objektet
felhantering
en metod som checkar om cirkelinstansen är en enhetscirkel
en metod som checkar om rektangelinstansen är en kvadrat

"""




# Refactoring with @dataclass and int

#TODO Make this @abstract instead (?)

@dataclass
class Shape:
    position: tuple

    # Read-only @property, getters
    @property
    def position(self) -> tuple:

        print("pos getter running")

        return self._position

    # Setter
    @position.setter
    def position(self, value):

        print("position setter running")

        if not isinstance(value, (tuple)):
            raise TypeError(f"Position must be tuple not {type(value)}")
        self._position = value

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

class Rectangle(Shape):
    """Rectangle. Inherits from Shape."""
    def __init__(self, position: tuple, width: float, height: float) -> None:
        
        super().__init__(position)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return self.width * 2 + self.height *2


    # Operator overloading for size equality.
    def __eq__(self, other: Shape):
        """Checks if shapes have identical size."""
        if self.width == other.width and self.height == other.height:
            return True
        else: return False

    # Operator overloading for area comparison
    def __lt__(self, other) -> bool:
        if self.Area < other.Area: return True
        else: return False
        
    def __le__(self, other) -> bool:
        if self.Area <= other.Area: return True
        else: return False

    def __gt__(self, other) -> bool:
        if self.Area > other.Area: return True
        else: return False
        
    def __ge__(self, other) -> bool:
        if self.Area >= other.Area: return True
        else: return False

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Circle(Shape):
    """Circle. Inherits from Shape."""
    def __init__(self, position: tuple, radius: float) -> None:
        
        super().__init__(position)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


# square1 = Rectangle((0,0),12,12)
# square2 = Rectangle((0,0),12,11)

# print(square1.area < square2.area)

#square2 = Rectangle((0,0),2,2)