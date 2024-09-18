from math import pi

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
        if self.radius <= 0:
            self.radius = 1
    
    def diameter(self):
        return (self.radius ** 2)
    
    def circumference(self):
            return (2 * pi * self.radius)



def radius_validation():
    c = Circle(-42)
    assert c.radius == 1, "Radius was not changed to correct fallback value."

def radius_test():
    c = Circle(5)
    assert c.radius == 5, "Radius instance attribute set incorrectly."

def diameter_test():
    c = Circle(8)
    assert c.diameter() == 16, "Diameter incorrect"

def circumference_test():
    c = Circle(10)
    assert round(c.circumference(), 2) == 62.83, "Circumference incorrect"

if __name__ == "__main__":
    functions_to_run = [
        radius_validation,
        radius_test,
        diameter_test,
        circumference_test
    ]

    for fn in functions_to_run:
        try:
            fn()
            print(f"Passed {fn.__name__}!")
        except Exception as e:
            print(f"{e} @ {fn.__name__}")