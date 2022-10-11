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

# Refactoring with @dataclass and ints

@dataclass
class Shape:
    position: tuple
    size: tuple

    # Read-only @property, getters
    @property
    def position(self) -> tuple:
        print("pos getter running")
        return self._x_pos

    @property
    def size(self) -> int:
        print("size getter running")
        return self._size

    
    # Setters
    @position.setter
    def position(self, position):
        print("position setter running")
        if not isinstance(position, (tuple)):
            raise TypeError(f"value must be tuple not {type(position).__name__}")
        self._value = position

    @size.setter
    def size(self, size):
        print("size setter running")
        if not isinstance(size, (tuple)):
            raise TypeError(f"value must be tuple not {type(size).__name__}")
        self._value = size

square1 = Shape((1,1),(1,1))

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