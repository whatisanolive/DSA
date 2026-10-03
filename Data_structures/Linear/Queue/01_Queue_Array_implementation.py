class Queue:
    def __init__(self):
        
        self.items = []
        self._size = 0

    def __len__(self):
        return self._size
    
    def __repr__(self):
        if not self.items:
            return "Empty queue"
        return ",".join(str(item) for item in self.items)
    

    def push(self,item):
        self.items.append(item)
        self._size += 1

    def pop(self):
        if not self.items:
            return False
        
        return self.items.pop(0)
    
    def peek(self):
        if not self.items:
            return "empty queue"
        
        return self.items[0]
    

if __name__ == '__main__':
    q = Queue()
    print(q)

    q.push(3)
    q.push(13)
    q.push(37)
    q.push(42)
    print("After pushing 3 elements: ",q)
    print("Length of queue: ", len(q))

    print("Peeking: ", q.peek())
    print("Popped item: ", q.pop())
    print("Queue after popping: ", q)