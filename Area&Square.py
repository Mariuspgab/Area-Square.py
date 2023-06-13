class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):

    def __init__(self,length, width):
          super().__init__(length,width)

    def area(self):
        return self.width*self.length


class Cube(Rectangle):

    def __init__(self,length, width,height):
          super().__init__(length, width)
          self.height=height
    def volume(self):
        return self.width*self.length*self.height


square= Square(3,3)

cube= Cube(3,3,3)

print(square.area())
print(cube.volume())
