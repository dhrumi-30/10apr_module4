#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
class Circle:
    def set_radius(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14159 * self.radius ** 2

    def compute_perimeter(self):
        return 2 * 3.14159 * self.radius


circle = Circle()
circle.set_radius(5)
area = circle.compute_area()
perimeter = circle.compute_perimeter()
print("The area of the circle is:", area)
print("The perimeter of the circle is:", perimeter)
