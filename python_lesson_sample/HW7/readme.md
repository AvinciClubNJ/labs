## Homework Week 7

#### 1. Same ***[requirement](https://github.com/AvinciClubNJ/labs/tree/master/python_lesson_sample/HW5)*** as homework 5 .
#### 2. Rewrite your program using OOP.
  2.1. Copy the code below to your program and implement the "Store" class. 

```python

# Store class to manage store items
class Store:
  # Constructor
  # Params:
  #  storeCapacity - maximum number of items the store can hold
  def __init__(self, storeCapacity):
    pass

  # Add one item
  # Params:
  #  name - item name to be added
  #  amount - item amount to be added
  # Return:
  #  True - item added successfully.
  #  False - item not added for some reason. One good reason could be store is full already.
  def addOneItem(self, name, amount):
    pass
  
  # Delete one item
  #  Params:
  #   name - item name to be deleted
  #  Return:
  #   True - item deleted successfully
  #   False - item failed to delete for some reason. One good reason could be the item not found in the store
  def deleteOneItem(self, name):
    pass
  
  # Check whether store is full
  #  Return:
  #   True - store is full
  #   False - Store is not full
  def isFull(self):
    pass
```
  2.2. Rewrite your program of homework 5 using class "Store"
#### 3. Extend your program to add another choice of "delete an item".