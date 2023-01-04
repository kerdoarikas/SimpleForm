from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return pi * self.radius ** 2


    def get_perimeter(self):
        return 2 * pi * self.radius

    def show_circle_data(self):
        print('Radius', self.radius)
        print('Diameter', self.get_diameter())
        print('Area', self.get_area())
        print('Perimeter', self.get_perimeter())