# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:16:29 2018

@author: cdh66
"""

class Node:
    def __init__(self,item):
        self.val = item
        self.next = None
        
class LinkedList:
    def __init__(self,item):
        self.head = Node(item)
        
    def add(self,item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
        
    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next
            
    def remove(self,item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print('does not exist')
            
    def removeItem(self,item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode= cur.next.next
                cur.next = nextnode
                break
        
ll = LinkedList(3)
print(ll.head.val, ll.head.next)

ll.add(4)

print(ll.head.val,ll.head.next.val,ll.head.next.next)

ll.add(1)
ll.add(5)

ll.remove(3)

ll.printlist()

ll.remove(5)
ll.printlist()


        

