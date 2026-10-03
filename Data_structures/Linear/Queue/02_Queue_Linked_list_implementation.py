class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __repr__(self):
        if not self.first:
            return "Empty queue"
        
        curr = self.first
        items = []
        while curr:
            items.append(str(curr.val))
            curr = curr.next

        return ', '.join(items)
    
    def __len__(self):
        return self._size


    def push(self, item):
        new_node = Node(item)
        curr = self.last

        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self._size += 1

    def pop(self):
        if not self.first:
            return "Empty queue"
        else:
            popped = self.first.val

            if self.first == self.last:
                self.first = self.last = None
                self._size -=1
                return popped
            else:
                self.first = self.first.next
                self._size -=1
                return popped
            
    def peek(self):
        if not self.first:
            return "Empty queue"
        else:
            return self.first.val
            
    
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



