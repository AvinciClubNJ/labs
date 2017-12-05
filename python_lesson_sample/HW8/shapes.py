#!/usr/bin/env python

# super and child classes

class myShapeClass(object):
    def __init__(self, c, cf):
        self._shapeColor = c
        self._circumference = cf

    def setColor(self, color):
        self._shapeColor = color

    def getColor(self):
        return self._shapeColor

    def calculateCircumference(self):
        pass

    def getCircumference(self):
        return self._circumference

class myTriangleClass(myShapeClass):
    def __init__(self, x, y, z):
        super().__init__("Blue", 0)
        self._side1 = x
        self._side2 = y
        self._side3 = z

    def calculateCircumference(self):
        self._circumference = self._side1 + self._side2 + self._side3


myTriangle = myTriangleClass(80, 80, 80)
myTriangle.calculateCircumference()
print("My triangle circumference is ", myTriangle.getCircumference())
print("My triangle color is ", myTriangle.getColor())
