# Store class to manage store items
class Store:
  # Constructor
  # Params:
  #  storeCapacity - maximum number of items the store can hold
  def __init__(self, storeCapacity):
    self.__store = {}
    self.__capacity = storeCapacity

  # Add one item
  # Params:
  #  name - item name to be added
  #  amount - item amount to be added
  # Return:
  #  True - item added successfully.
  #  False - item not added for some reason. One good reason could be store is full already.
  def addOneItem(self, name, amount):
    if self.isFull():
      return False
    else:
      self.__store[name] = amount
      return True
  
  # Delete one item
  #  Params:
  #   name - item name to be deleted
  #  Return:
  #   True - item deleted successfully
  #   False - item failed to delete for some reason. One good reason could be the item not found in the store
  def deleteOneItem(self, name):
    if name in self.__store:
      del self.__store[name]
      return True
    else:
      return False
  
  # Get all items
  #  Return:
  #   dictionary with item name as key and item amount as value
  def getAllItems(self):
    return self.__store

  # Check whether store is full
  #  Return:
  #   True - store is full
  #   False - Store is not full
  def isFull(self):
    return (len(self.__store) >= self.__capacity)


def printMainMenu():
  print("Main menu:")
  print(" 1. Add item to store")
  print(" 2. Delete item from store")
  print(" 3. Display all items")
  print(" 4. Exit")
  print("")

def chooseTask():
  strChoice = input("Please type your choice(1, 2 , 3): ")
  choice = 0
  if strChoice.isdigit():
    choice = int(strChoice)
  else:
    choice = -1
  return choice

def addItem():
  name = input("Please type item name: ")
  amount = 0
  while True:
    strAmount = input("Plesae type item amount: ")
    if strAmount.isdigit():
      amount = int(strAmount)
      break
    else:
      print("amount need to be a number.")
  g_store.addOneItem(name, amount)
  print("")

def deleteItem():
  name = input("Please type item name: ")
  if g_store.deleteOneItem(name):
    print("Item \"" + name + "\" has been deleted.")
  else:
    print("Item \"" + name + "\" not found.")
  

def printAllItems():
  print("$$$$$$$$$$$$$$$$$$$$$$$$$")
  print("All items in store: ")
  allItems = g_store.getAllItems()
  for i in allItems:
    print("  " + i + ": " + str(allItems[i]))
  print("$$$$$$$$$$$$$$$$$$$$$$$$$")
  print("")

def isStoreFull():
  return g_store.isFull()

  
# Main program
g_store = Store(5)
while True:
  # Print main menu
  printMainMenu()
  
  # Get user's choice
  choice = chooseTask()
  
  # Choice 1: add item to store
  if choice == 1:
    addItem()

  #Choice 2: delete an item from store
  elif choice == 2:
    deleteItem()
    
  #Choice 3: print all items
  elif choice == 3:
    printAllItems()
  
  # Choice 4: Exit
  elif choice == 4:
    print("Bye!")
    break
  
  # Other choices
  else:
    print("Please type a number between 1 and 3.")
    print("")
    continue
  
  # If store is full
  if isStoreFull():
    printAllItems()
    print("Store is full! Bye!")
    break
