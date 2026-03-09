from slistHT import SList

class SList2(SList):
    
    def removeNtoM(self,n,m):          
        if self.isEmpty():
            return
        
        #check input parameters
        if (n>m) or m>=len(self):
            print ("invalid input parameters")
            return
      
        node=self._head
        prev = None
    
        for i in range (n):
            prev = node
            node=node.next
        for i in range (n,m+1):
            node=node.next
            
        if prev:
            prev.next = node
        else:
            self._head = node
            
        if (m==len(self)-1):
          self.tail = prev
            
        self._size -=(m-n+1)
                   
            
       
                
                   
if __name__=='__main__': 

    l=SList2()
    for i in [0,1,2,3,4,5]:
        l.addLast(i)
    print(l)
    l.removeNtoM(2,4)
    print(l)
    print("---")
    
    l=SList2()
    for i in [0,1,2,3,4,5]:
        l.addLast(i)
    l.removeNtoM(0,2)
    print(l)
    print("---")
    
    l=SList2()
    for i in [0,1,2,3,4,5]:
        l.addLast(i)
    l.removeNtoM(3,5)
    print(l)
    print("---")
    
    l.removeNtoM(0,1)
    print(l)
    print("---")
    
    l.removeNtoM(3,5)
    print(l)
    
    print("---")
    l.removeNtoM(0,0)
    print(l)