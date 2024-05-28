class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * 3.14 * self.radius
    def area(self):
        return 3.14 * self.radius * self.radius

radius = int(input("Enter radius of the circle: "))
circle1 = Circle(radius)
print(f"Circumference of circle of radius {radius} = {int(circle1.circumference())}")
print(f"Area of circle of radius {radius} = {circle1.area()}")
# print(f"Area of circle of radius {radius} = {circle1.area()} unit\u00B2")