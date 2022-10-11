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

# Refactoring with @dataclass and int

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

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - #

class Rectangle(Shape):
    """Rectangle. Inherits from Shape."""
    def __init__(self, position: tuple, width: float, height: float) -> None:
        super().__init__(position)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.height * self.width

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

# @dataclass
# class Circle(Shape):
#     pass

# @dataclass
# class Rectangle(Shape):
#     pass

# @dataclass
# class Square(Rectangle):





# @dataclass
# class Shape:
#     """Parent class with positional data."""

#     #def __init__(self, position: float, size: tuple, opacity: int, velocity: float) -> None:
#     #    self.position=position
#     #    self.size=size
#     #    self.opacity=opacity
#     #    self.velocity=velocity

#     position: float
#     size: tuple
#     opacity: int
#     velocity: float

#     @property
#     def position(self) -> float:
#         return self._position

#     @property
#     def size(self) -> tuple:
#         return self._size
   
#     @property
#     def opacity(self) -> int:
#         return self._opacity

#     @property
#     def velocity(self) -> float:
#         return self._velocity

#     @position.setter
#     def position(self, value: float):
#         if not isinstance(value, (float)):
#             raise TypeError(f"Must be tuple, not {type(value)}")
        
#         if len(value) < 1:
#             raise ValueError(f"Point need at least x and y value.")
        
#         self._position = value
    
#     @size.setter
#     def size(self, value: tuple):
#         if not isinstance(value, (tuple)):
#             raise TypeError(f"Must be tuple, not {type(value)}")

#         self.size = value

#     @opacity.setter
#     def opacity(self, value: int):
#         if not isinstance(value, (int)):
#             self.opacity=1.0
#             raise TypeError(f"Must be int, not {type(value)}")

#         self.opacity = value

#     @velocity.setter
#     def opacity(self, value: int):
#         if not isinstance(value, (int)):
#             self.velocity=1.0
#             raise TypeError(f"Must be int, not {type(value)}")

#         self.velocity = value

#     # __repr__ created with @dataclass
#     # def __repr__(self) -> None:
#     #     return f"{self.position}, {self.area} {self.opacity}, {self.velocity}"


# # --- Comparators --- # 
# # To find out the area of a complex shape, we can track if a randomly placed dot is withing the shape
# # TODO: Implement get_area/get_volume method for complex shapes

# class Cube(Shape):
#     """Inherits from Shape."""

#     def get_volume(self):
#         return self.size[0] * self.size[1] * self.size[2]

# class Rectangle(Cube):
#     """Inherits from Cube."""

#     def get_area(self, length, ):
#         return self.size[0] * self.size[1]


#  # --------------- #


# class Sphere(Shape):
#     """Inherits from Shape."""
#     def volume(self):
#         return self.size[0] * self.size[1] * self.size[2]

# class Torus(Sphere):
#         """Child class for Torus, inherits from Sphere."""

# class Ring(Torus):
#     """Child class for Ring, inherits from Torus."""

# class Circle(Shape):
#         """Child class for Circle, inherits from Torus."""
# if __name__ == "__main__":
#     square1 = Rectangle((2.2,0.0),(5.0,5.0))
#     print(square1)