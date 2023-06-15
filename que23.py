#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle()
rectangle.set_dimensions(5, 3)
area = rectangle.compute_area()
print("The area of the rectangle is:", area)
