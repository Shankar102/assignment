#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def findPair(nums, target):
 
    for i in range(len(nums) - 1):
 
        for j in range(i + 1, len(nums)):
 
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)


# In[ ]:


#2
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[ ]:


#3
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    if size1 != size2:
        return 0
 
    temp = string1 + string1
 
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")


# In[ ]:


#4
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 

string = "shankarsahu"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])
 


# In[ ]:


#5
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

n = 4
TowerOfHanoi(n, 'A', 'C', 'B')


# In[ ]:


#6

s = "*-A/BC-/AKL"


stack = []

operators = set(['+', '-', '*', '/', '^'])

s = s[::-1]

for i in s:

    if i in operators:


        a = stack.pop()
        b = stack.pop()

        temp = a+b+i
        stack.append(temp)


    else:
        stack.append(i)


print(*stack)


# In[ ]:


#7
def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
           
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# In[ ]:


#8
def areBracketsBalanced(expr):
    stack = []
 
   
    for char in expr:
        if char in ["(", "{", "["]:
 
          
            stack.append(char)
        else:
 
           
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                     return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
 
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 


# In[ ]:


#9
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 

def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)

def createStack():
    stack = []
    return stack
def isEmpty( stack ):
    return len(stack) == 0

def push( stack, item ):
    stack.append( item )
 

def pop( stack ):

    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
    stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)


# In[ ]:


#10
  def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))
          
  
    __repr__=__str__
      
    
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
  
  

    def isEmpty(self):
       
        if self.top == None:
            return True
        else:
        
            return False
  

    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
     
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else: 
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
  
    
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
          
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))
  
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print ("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))
  
                  
              

stack = Stack() 
  
stack.push(3)
stack.push(5) 
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()     
stack.pop()
stack.getMin()
stack.pop() 
stack.peek()

