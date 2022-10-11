from __future__ import annotations
from dataclasses import dataclass
import math

#TODO finish before deadline

"""
override av __str__

x och y som representerar mittpositionen av objektet

en metod som checkar om en viss punkt befinner sig innanför objektet
felhantering

"""

# Refactoring with @dataclass

#TODO Make this @abstract instead (?)

@dataclass(repr=False)
class Shape:
    """
    Parent class.
    
    An abstract(?) class. Shouldn't be instantiated on its own.

    Attributes
    ----------
    position : tuple
        Values representing the center position of the object (x,y,z.. etc).

    Methods
    ----------
    translate_position(position: tuple)
        Call as normal class method to update positional data of given shape.

    """

    position: tuple

    @property # Read-only, getter
    def position(self) -> tuple:
        print("position getter running")
        return self._position

    @position.setter # Read and write, setter
    def position(self, value: tuple):
        """Sets position to given value."""

        print("position setter running")

        if not isinstance(value, (tuple)):
            raise TypeError(f"Position must be tuple not {type(value)}")
        self._position = value


    def translate_position(self, position: tuple) -> tuple:
        """
        Callable method to translate positional values (center point) of shape.

        Same as typing 'object.position = (tuple)' except translate_position()
        stores old positional values in variable 'old_pos'.

        """

        print("translate_position running")

        # Stores previous position
        old_pos = self.position
                # TODO: add meaning to this variable (maybe animating path or something)

        # Updates position to new value
        self.position = position

        print(f"{old_pos=}, new={position}")

        return self.position
        
    def __repr__(self):
        return f"{self.__class__.__name__}, midpoint at {self.position}.)"

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

class Rectangle(Shape):
    """
    Child class of Shape.
    
    Contains width, height, area and perimeter.

    Attributes
    ----------
    width: float
        Width (x) of rectangle.

    height: float
        Height (y) of rectangle.

    area: float
        Area of rectangle.

    perimeter: float
        Perimeter of rectangle.

    Methods
    -------
    is_square(width: float, height: float)
       Return True if width == height.

    overloaded __eq__, __lt__, __le__, __gt__, __ge__

    """

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

    def is_square(self, width: float, height: float) -> bool:
        """Checks if given rectangle is square."""

        if self.width == self.height:
            return True
        else: return False

    # Operator overloading for size equality.
    def __eq__(self, other: Shape) -> bool:
        """Checks if any two given rectangles are identical in size."""

        if self.width == other.width and self.height == other.height:
            return True
        else: return False

    # Operator overloading for area comparison
    def __lt__(self, other: Shape) -> bool:
        if self.Area < other.Area: return True
        else: return False
        
    def __le__(self, other: Shape) -> bool:
        if self.Area <= other.Area: return True
        else: return False

    def __gt__(self, other: Shape) -> bool:
        if self.Area > other.Area: return True
        else: return False
        
    def __ge__(self, other: Shape) -> bool:
        if self.Area >= other.Area: return True
        else: return False

    def __repr__(self):
        return f"{self.__class__.__name__} -- midpoint at {self.position} -- {self.area=}.)"

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Circle(Shape):
    """
    Child class of Shape.
    
    Contains radius, area and circumference.

    Attributes
    ----------
    width: float
        Width (x) of circle.

    height: float
        Height (y) of circle.

    area: float
        Area of circle.

    circumference: float
        Circumference of circle.

    Methods
    -------

    """
    def __init__(self, position: tuple, radius: float) -> None:
        
        super().__init__(position)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return math.pi * self.radius * 2


    def is_unit_circle(self, width: float, height: float) -> bool:
        """Should check if given circle is unit."""
        return True

    def __repr__(self):
        return f"{self.__class__.__name__} -- midpoint at {self.position} -- {self.radius=}.)"
