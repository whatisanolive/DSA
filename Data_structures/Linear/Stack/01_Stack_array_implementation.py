# stack - Linked List implementation

class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        elements = [str(item) for item in reversed(self.items)]
        return ", ".join(elements)

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
    
    def is_empty(self):
        return self.items == []
    

if __name__ == '__main__':
    stack = Stack()
    print("Stack is empyt: ",stack.is_empty())
    stack.push(10)
    stack.push(7)
    stack.push(15)
    stack.push(13)
    stack.push(1)
    stack.push(0)


    print("stack: ", stack)

    print("peek: ",stack.peek())

    print("popped : ", stack.pop())

    print("popped : ", stack.pop())

    print("stack: ", stack)

    print("Stack is empty: ",stack.is_empty())



#  len() has time complexity of 1

# pop(n) has time complexity of O(n) on average, but , pop()/pop(-1) has O(-1)

# to check an empty list: self.items == [] -> O(1) SLOWER,  Python has to allocate a new, temporary empty list object [] in memory, and then perform a value comparison between the two lists.
#  not self.items -> O(1) FASTER,  It immediately checks the list's internal size attribute. If the size is 0, it returns True.

#list.reversed() - inplace (returns None), reverse(list) - returns the reversed list