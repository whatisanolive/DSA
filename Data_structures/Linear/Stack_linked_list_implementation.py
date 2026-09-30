# stack - Linked List implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top =  None
        self.size = 0

    def __len__(self):
        return self.size
    
    # O(n)
    def __repr__(self):
        items = []
        curr = self.top
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return ", ".join(items)

    # O(1)        
    def push(self,data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1
        

    # O(1)
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is emptyx")

        popped_value = self.top.data
        self.top = self.top.next
        self.size -=1

        return popped_value

    #O(1)
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        
        return self.top.data
    #O(1)
    def is_empty(self):
        return self.top is None
    
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

    print("Stack is empyt: ",stack.is_empty())
        