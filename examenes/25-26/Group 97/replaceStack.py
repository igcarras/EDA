class Stack:
       
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0
   
    def push(self, e):
        self.items.append(e)
    
    def pop(self):
        if self.isEmpty():
            print('Error: Stack is empty')
            return None
        return self.items.pop()
    
    def top(self):
        if self.isEmpty():
            print('Error: Stack is empty')
            return None
        return self.items[-1]
    

def ReplaceStack(s,old,new):

    if(s==[] or s == None):
        return None
    
    aux = Stack()
    
    print("Original stack:")
    print(str(s)  + "\n")
    while not s.isEmpty():
        e = s.pop()
        if (e == old):
            aux.push(new)
        else:
            aux.push(e)
    
    print("Intermmediate stack:")
    print(str(aux) + "\n")
        
    #The stack must be reversed
    while not aux.isEmpty():
        s.push(aux.pop())
    
    print("Final stack:")
    print(str(s))
    
    return s
    
"""Test cases"""
mystack = Stack()

mystack.push(5)
mystack.push(1)
mystack.push(3)
mystack.push(2)
mystack.push(6)
mystack.push(5)
mystack.push(5)

print("Input stack: " + str())

ReplaceStack(mystack,5,0)

print("Output Stack: " + str())


""" Complaxity is O(n) """
