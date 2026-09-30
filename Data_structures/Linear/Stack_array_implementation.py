# stack - Linked List implementation

class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        pass

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.items :
            return None
        return self.items.pop(-1)
    
    def peek(self):
        if not self.items :
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)



#  len() has time complexity of 1
# pop(n) has time complexity of O(n) on average, but , pop()/pop(-1) has O(-1)