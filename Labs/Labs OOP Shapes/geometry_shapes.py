from __future__ import annotations
from dataclasses import dataclass

#TODO finish before deadline

"""
Class should have:

area property
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

class Shape:
    """Parent class with positional data."""

    def __init__(self, position: tuple, size: tuple, opacity: int, velocity: float) -> None:
        self.position=position
        self.size=size
        self.opacity=opacity
        self.velocity=velocity

    @property
    def position(self) -> tuple:
        return self._position

    @property
    def size(self) -> tuple:
        return self._size
   
    @property
    def opacity(self) -> int:
        return self._opacity

    @property
    def velocity(self) -> float:
        return self._velocity

    @position.setter
    def position(self, value: tuple):
        if not isinstance(value, (tuple)):
            raise TypeError(f"Must be tuple, not {type(value)}")
        
        if len(value) < 1:
            raise ValueError(f"Point need at least x and y value.")
        
        self._position = value
    
    @size.setter
    def size(self, value: tuple):
        if not isinstance(value, (tuple)):
            raise TypeError(f"Must be tuple, not {type(value)}")

        self.size = value

    @opacity.setter
    def opacity(self, value: int):
        if not isinstance(value, (int)):
            self.opacity=1.0
            raise TypeError(f"Must be int, not {type(value)}")

        self.opacity = value

    @velocity.setter
    def opacity(self, value: int):
        if not isinstance(value, (int)):
            self.velocity=1.0
            raise TypeError(f"Must be int, not {type(value)}")

        self.velocity = value


    def __repr__(self) -> None:
        return f"{self.position}, {self.area} {self.opacity}, {self.velocity}"


# --- Comparators --- # 
# To find out the area of a complex shape, we can track if a randomly placed dot is withing the shape
# TODO: Implement get_area/get_volume method for complex shapes

class Cube(Shape):
    """Inherits from Shape."""

    def get_volume(self):
        return self.size[0] * self.size[1] * self.size[2]

class Rectangle(Cube):
    """Inherits from Cube."""

    def get_area(self, length, ):
        return self.size[0] * self.size[1]


 # --------------- #


class Ring(Shape):
    """Inherits from Shape."""
    def volume(self):
        return self.size[0] * self.size[1] * self.size[2]

class Torus(Shape):
        """Child class for circle, inherits from Shape."""

class Circle(Shape):

    def __init__(self, position: tuple, radius: float) -> None:
        super().__init__(position)
        self.radius = radius

if __name__ == "__main__":
    square1 = Rectangle((2.2,0.0),(5.0,5.0))
    print(square1)