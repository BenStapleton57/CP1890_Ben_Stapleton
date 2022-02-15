import math

class Circle:
    def __init__(self, radius: int):
        self.__radius = radius

    @property
    def radius_length(self):
        return self.__radius

    @radius_length.setter
    def radius_length(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            raise ValueError(f'Radius must be greater than Zero')

    def get_area(self):
        area = math.pi * (self.radius_length **2)
        return area

small_circle = Circle(10)
big_circle = Circle(500)

print(small_circle.get_area())
print(big_circle.get_area())
