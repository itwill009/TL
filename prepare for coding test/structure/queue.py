class Queue:
    
    def __init__(self):
        self.items = []
        
    def enque(self,item):
        self.items.insert(0,item)
    
    def deque(self):
        self.items.pop()
        
    def print_que(self):
        print(self.items)
        
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
queue = Queue()

queue.is_empty()
queue.enque(1)

queue.print_que()

queue.enque(5)

queue.print_que()

queue.deque()

queue.print_que()

queue.deque()

queue.print_que()
