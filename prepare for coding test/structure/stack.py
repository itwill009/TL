# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:01:07 2018

@author: cdh66
"""

class Stack:
    def __init__(self):
        self.items = []
        self.max = 5
        
    def push(self,items):
        if len(self.items) < 5:
            self.items.append(items)
        else:
            print('full stack')
            
    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print('empty stack')
            
    def print_stack(self):
        print(self.items)
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    
st = Stack()

print(st.is_empty())

st.push(1)
st.print_stack()
st.push(2)
st.print_stack()
st.push(3)
st.print_stack()

st.pop()
st.print_stack()

print(st.peek())
print(st.is_empty())


        