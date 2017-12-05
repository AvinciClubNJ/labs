## Homework 8

### Requirements

#### 1. Define a base class for "Shape" with following data and methods

The base/super class should have its own data member, "color" and "circumference"

The base class should provide functions to set/get shape color and calculate circumference.

See sample code. Or write your own.

**Note: Fill in codes for functions if applicable.**

```python

# Shape class
class Shape:
    # Constructor
    def __init__(self):
        pass

    def setColor(self, color):
        pass

    def getColor(self):
        pass

    def draw(self):
        pass

    def getCircumference(self):
        pass


```

#### 2. Define 3 child classes with "Shape" as their parent, implement child functions.

Circle

Triangle

Rectangle

**Note: To utilize Turtle, you need to use Python version 2.7. However, super() functions differently in Python 2.7 and Python 3. For simplicity, do not use super in __init__ in child class.
I included a sample code in the same directory to show how to call super() in child init.**

#### 3. Declare 3 instances, one for each child class, set color, get its circumference, and draw

3.1 Create circle instance "myCircle" with radius 50, color red

3.2 Create triangle instance "myTriangle" with same length 100 for all sides, and color blue

3.3 Create rectangle instance "myRectangle" with width 50 and length 100, and color yellow

3.4 Print out the circumference for each

3.5 Call draw function for each, you will decide where to draw the shape.
