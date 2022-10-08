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
    def __init__(self, area: float | int, circumference: float | int, position: tuple) -> None:
        self.area = area
        self.circumference = circumference
        self.position = position

class Square(Shape):
    pass

class Circle(Shape):
    pass

square1 = Square(25.0,20.0,[0.0,0.0])