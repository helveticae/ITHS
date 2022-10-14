from __future__ import annotations
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt

@dataclass(repr=False)
class Shape:
    """
    Used to instantiate shapes (2D and 3D).
    
    Forces all shape to have positional values. Shouldn't be instantiated on its own.

    Attributes
    ----------
    position : tuple
        Values representing the center position of the object (x,y,z.. etc).
    
    Methods
    ----------
    translate_position()
        Call as normal class method to update positional data of given shape.

    operators overloaded for area comparison: __eq__, __lt__, __le__, __gt__, __ge__
    
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

        #TODO Throw ValueError if points in position tuple < object dimensions
        #i.e. a 3D object must cover at least 3 points in space, etc.

        self._position = value

    def translate_position(self, position: tuple) -> tuple:
        """
        Callable method to translate positional values (center point) of shape.

        Same as typing 'object.position' except translate_position() stores previous positional values in variable 'old_pos'.
        """

        print("translate_position running")

        # Stores previous position TODO: add meaning to this variable (maybe animate path or something(?))
        old_pos = self.position

        # Updates position to new value
        self.position = position

        print(f"{old_pos=}, new={position}")

        return self.position

    # Operator overloading for equality in area.
    def __eq__(self, other: Shape) -> bool:
        print("__eq__ called from Shape class")
        """Checks if any two given shapes are identical in area."""

        if self.width == other.width and self.height == other.height:
            return True
        else: return False

    # Continue overloading <, <=, >, >=
    def __lt__(self, other: Shape) -> bool:
        print("__lt__ called from Shape class")

        if self.area < other.area: return True
        else: return False
        
    def __le__(self, other: Shape) -> bool:
        print("__le__ called from Shape class")

        if self.area <= other.area: return True
        else: return False

    def __gt__(self, other: Shape) -> bool:
        print("__gt__ called from Shape class")

        if self.area > other.area: return True
        else: return False
        
    def __ge__(self, other: Shape) -> bool:
        print("__ge__ called from Shape class")

        if self.area >= other.area: return True
        else: return False

    # str & repr
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return str(self.__dict__)
        
class Rectangle(Shape):
    """
    Child class Rectangle. Inherits from Shape. Contains width, height, area and perimeter.

    Attributes
    ----------
    width: float
        Width (x) of rectangle.
    height: float
        Height (y) of rectangle.
    area: float
        Area (A) of rectangle.
    perimeter: float
        Perimeter (P) of rectangle.

    Methods
    -------
    is_square()
       Returns True if width == height.

    get_vertices()
        Calculates four corner points from square center point using width and height.

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
        "Returns width and height * 2"
        return (self.width + self.height) * 2

    def is_square(self, width: float, height: float) -> bool:
        """Checks if given rectangle is square."""

        if self.width == self.height: return True
        else: return False

    def get_vertices(self) -> tuple:
        """Returns points P and Q from width, height and position."""

        P1 = ((self.position[1] + self.width /-2, self.position[0] + self.height /2))# top left
        P2 = ((self.position[1] + self.width /2, self.position[0]+ self.height /2)) # top right
        Q1 = ((self.position[1] + self.width /-2, self.position[0] + self.height /-2))# bottom left
        Q2 = ((self.position[1] + self.width /2, self.position[0] + self.height /-2)) # bottom right

        return [(P1,P2),(Q1,Q2)]
        # Probably a better way to do this...


    def point_inside(self, input_point: tuple) -> bool:
        """Returns True if given point is inside rectangle."""
    # Not correct, redo.
    # def point_inside(self, input_point: tuple) -> bool:
    #     "Returns True if given point is inside square."



    def __repr__(self):
        return f"{self.__class__.__name__} -- midpoint at {self.position} -- {self.area=}.)"

class Circle(Shape):
    """
    Child class Circle. Inhertis from Shape. Contains radius, area and circumference.

    Attributes
    ----------
    radius: float
        Radius (r) of circle.
    area: float
        Area (A) of circle.
    circumference: float
        Circumference (C) of circle.

    Methods
    -------
    is_unit_circle()
        Returns True if circle position is 0.0 and radius is 1.

    point_inside()
        Returns True if given point is inside circle.
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

    def is_unit_circle(self) -> bool:
        "Returns True if circle position is 0.0 and radius is 1."

        if self.radius == 1 and self.position[0] == 0 and self.position[1] == 0:
            return True
        else:
            return False

    # redo this
    def point_inside(self, input_point: tuple) -> bool:
        "Returns True if given point is inside circle."
        
        if math.dist(self.position, input_point) <= self.radius:
            return True
        else:
            return False

 # Operator overloading for equality in area.
    def __eq__(self, other: Shape) -> bool:
        """Checks if any two given 2D shapes are identical in area."""
        print("__eq__ called from Circle class")
        
        if self.area == other.area: return True
        else: return False

    def __repr__(self):
        return f"{self.__class__.__name__} -- midpoint at {self.position}, {self.radius=}, {self.area=}.)"

class Sphere(Circle):
    """
    Child class Sphere. Inhertis from Circle. Contains radius, volume and surface area.

    Attributes
    ----------
    radius: float
        Radius (r) of sphere.
    volume: float
        Volume (V) of sphere.
    surface_area: float
        Surface area (A) of sphere.

    Methods
    -------
    n/a
    """

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    @property
    def surface_area(self):
        return 4 * math.pi * self.radius * 2
    
    # Operator overloading for volume equality.
    def __eq__(self, other: Shape) -> bool:
        """Checks if any two given shapes are identical in volume."""
        print("__eq__ called from Sphere class")

        if self.volume == other.volume: return True
        else: return False

    def __lt__(self, other: Shape) -> bool:
        print("__lt__ called from Sphere class")

        if self.volume < other.volume: return True
        else: return False
        
    def __le__(self, other: Shape) -> bool:
        print("__le__ called from Sphere class")

        if self.volume <= other.volume: return True
        else: return False

    def __gt__(self, other: Shape) -> bool:
        print("__gt__ called from Sphere class")

        if self.volume > other.volume: return True
        else: return False
        
    def __ge__(self, other: Shape) -> bool:
        print("__ge__ called from Sphere class")
        
        if self.volume >= other.volume: return True
        else: return False
     
class Cube(Rectangle):
    """
    Child class Cube. Inhertis from Rectangle. Contains width, height, length, surface area and and volume.

    Attributes
    -------
    width: float
        Width (x) of cube.
    height: float
        Height (y) of cube.
    length: float
        Length (z) of cube.
    volume: float
        Volume (V) of cube.
    surface_area: float
        Area (A) of cube.

    Methods
    -------
    n/a
    """

    def __init__(self, position: tuple, width: float, height: float, length: float) -> None:
        
        super().__init__(position, width, height)
        self.length = length

    @property
    def volume(self):
        return self.width * self.height * self.length

    @property
    def surface_area(self):
        return 6 * (self.width * self.height * self.length)

   # Operator overloading for VOLUME equality.
    def __eq__(self, other: Shape) -> bool:
        """Checks if any two given shapes are identical in volume."""
        print("__eq__ called from Cube class")

        if self.volume == other.volume:
            return True
        else: return False

    # Operator overloading for VOLUME comparison.
    def __lt__(self, other: Shape) -> bool:
        print("__lt__ called from Cube class")
        if self.volume < other.volume: return True
        else: return False
        
    def __le__(self, other: Shape) -> bool:
        print("__le__ called from Cube class")
        if self.volume <= other.volume: return True
        else: return False

    def __gt__(self, other: Shape) -> bool:
        print("__gt__ called from Cube class")
        if self.volume > other.volume: return True
        else: return False
        
    def __ge__(self, other: Shape) -> bool:
        print("__ge__ called from Cube class")
        if self.volume >= other.volume: return True
        else: return False

    def __repr__(self):
        return f"{self.__class__.__name__} -- midpoint at {self.position} -- {self.volume=}.)"
