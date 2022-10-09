from __future__ import annotations

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
    """Parent class with positional data. X/Y/Z position is stored in tuple."""

    def __init__(self, position: tuple) -> None:
        self.position=position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: tuple):
        if not isinstance(value, (tuple)):
            raise TypeError(f"Must be tuple, not {type(value)}")
        self._position = value

    def __repr__(self) -> None:
        return f"{self.position}"


    # --- Comparators --- # 
    # To find out the area of a complex shape, we can track if a randomly placed dot is withing the shape
    # TODO: Implement get_area/get_volume method for complex shapes


class Rectangle(Shape):
    """Child class for rectangle, inherits from Shape."""

    def __init__(self, position: tuple, size: tuple) -> None:
        super().__init__(position)
        self.size = size


class Circle(Shape):
    """Child class for circle, inherits from Shape."""

    def __init__(self, position: tuple, radius: float) -> None:
        super().__init__(position)
        self.radius = radius


if __name__ == "__main__":
    square1 = Rectangle((2.2,0.0),(5.0,5.0))
    print(square1)