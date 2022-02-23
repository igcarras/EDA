#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/isegura/EDA/blob/master/Balanced_parenthesis_extendido.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# #Balanced parenthesis 
# 
# Detecting when the parenthesis in an expression are correctly balanced or not is an important task to recognize many programming language structures (i.e. to evaluate arithmetic or logical expressions).
# 
# 
# In logical and arithmetic expressions, parentheses must appear in a balanced way. In other words:
# - 1) each opening symbol has a corresponding closing symbol and 
# - 2) the pairs of parentheses are properly nested. 
# 
# The following table shows examples of balanced and non balanced expressions of parenthesis:
# 
# | Balanced  | Non balanced |
# | --- | --- | 
# | (()()()()) | ((((((())|
# |(((()))) | ())) |
# | (()((())())) | (()()(()|
# 
# 
# Please, write a Python program that reads a string of parenthesis and determines if its parenthesis are balanced. 
# A stack is a good data structure to solve this problem because  closing symbols match opening symbols in the reverse order of their appearance. 
# 
# 
# Below, we explain the steps to implement the algorithm. Firstly, you must create an empty stack, which be used to store the opening symbols. Then, you must read the expression from left to right. For each symbol:
# - If the symbol is an opening symbol, add it on the stack (with push operation).
# - If the symbol is a closing symbol:
#     - If the stack is empty, there is no any opening symbol for it, so return false (the expression is not balanced). 
#     - Otherwise, remove the top of the stack (with pop) and continue. 
#         
# When you have read all characters in the expression, there  are two possibilities:
# a) The stack is not empty, which means that the expressions contained some opening symbols without their corresponding closing symbols. Therefore, you must return false. 
# b) The stack is empty. You must return true. 
# 
# 

# 

# In[13]:


class Stack:
  """LIFO Stack implementation using a Python list as storage. 
  The top of the stack stored at the end of the list."""
  
  def __init__(self):
    """Create an empty stack"""
    self._items=[]
    
  def __len__(self):
    """Return the number of elements in the stack"""
    return len(self._items)
  
  def isEmpty(self):
    """Return True if the stack is empty"""
    return len(self._items)==0
  
  def __str__(self):
    """returns a string representing the elements of the stack"""
    return str(self._items)

  def push(self,e):
    """Add the element e to the top of the stack"""
    self._items.append(e)
    
  def pop(self):
    """Remove and return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    return self._items.pop() #remove last item from the list
  
  def top(self):
    """Return the element from the top of the stack"""
    if self.isEmpty():
      print('Error: Stack is empty')
      return None
    
    #returns last element in the list
    return self._items[-1] 
  
  

  


# In[14]:


def balanced1(exp):
    """This functions takes a string, exp, and checks if its parenthesis are well-balanced. 
    This functions does not use break and has a single return"""
    stack = Stack()
    result=True
    i=0

    while result and i<len(exp):
        c=exp[i] 
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.isEmpty():
                result=False
            else:
                stack.pop()
        #else:#you don't need this else, 
            #we ignore the rest of characters
            #pass    

        i+=1

    
    return result and stack.isEmpty()


def balanced2(exp):
    """This functions takes a string, exp, and checks if its parenthesis are well-balanced. 
    This functions allows to use break and has a single return"""    
    stack = Stack()
    result=True
    for c in exp:
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.isEmpty():
                result=False
                break 
            else:
                stack.pop() 
        #else:#you don't need this else
            #we ignore the rest of characters
            #pass
                
    
    
    return result and stack.isEmpty()


def balanced3(exp):
    """This functions takes a string, exp, and checks if its parenthesis are well-balanced. 
    This functions allows to use several returns"""    
    stack = Stack()
    for c in exp:
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.isEmpty():
                return False
            stack.pop()
        #else:   #you don't need this else
            #we ignore the rest of characters
            #pass
          
    return stack.isEmpty()

  
  
print('((((((())',balanced3('((((((())'))
print('(()()()())',balanced3('(()()()())'))
print('(((())))',balanced3('(((())))'))
print('()))',balanced3('()))'))
print('(()()(()',balanced3('(()()(()')      )
print('(()((())()))',balanced3('(()((())()))')      )


# The previous function only works for parenthesis. Extend it in order to deal also with:
# 
#     Brace: ‘{‘ and ‘}
#     Brackets: ‘[‘ and ‘]’
# 
# You need to implement a function that takes an opening symbol, '(','{','[',   and a closing symbol, ')','}',']', and check that they belong to the same type of symbol. Below, you can find two different versions of this functions. 

# In[15]:


def sameType(a,b):
    """This functions checks if a and b belong to the same type of parenthesis"""
    if a=='(' and b==')':
        return True
    if a=='{' and b=='}':
        return True
    if a=='[' and b==']':
        return True
    
    return False
  

def sameType1(a, b):
    """This functions checks if a and b belong to the same type of parenthesis"""
    opening=['(','{','[']
    closing=[')','}',']']
    pos=opening.index(a)
    return b==closing[pos]
  
  

def balanced_ext(exp):
    """Checks if the parenthesis in the expression, exp, are well-balanced"""
    s=Stack()
    for c in exp:
        if c in [ '(' , '[' , '{' ] : #c=='(' or c=='{' or c=='[': 
            s.push(c)
        elif c in [ ')' , ']' , '}' ]: #c==')' or c=='}' or c==']'
            if s.isEmpty():
                return False
            else:
                o=s.pop()
                if not sameType(o,c):
                    return False

    
    return s.isEmpty()
    
exp='()'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='('
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='([])'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='([]'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='([]))'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='([]{})'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='([{}]{()})'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))

exp='()(()){([()])}'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))
exp='((()(()){([()])}))'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))

exp=')(()){([()])}'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))


exp='({[]})'
print('is balanced ext ({})={}'.format(exp,balanced_ext(exp)))


