"""
Grocery store
"""

class Grocery:

    def __init__(self):
        self.fruits = []
        return
  
    def set_fruits(self, fruit):
        self.fruits.append(fruit)
        return self.fruits
        
    def get_fruit(self, x):
        fruit = self.fruits[x]
        return fruit



grocery1 = Grocery()
grocery1.set_fruits("mango")
grocery1.set_fruits("apple")
grocery1.set_fruits("banana")
grocery1.set_fruits("grapes")
grocery1.set_fruits("orange")
# print(grocery1.fruits)
# print(grocery1.get_fruit(2))
print(grocery1.get_fruit(4))