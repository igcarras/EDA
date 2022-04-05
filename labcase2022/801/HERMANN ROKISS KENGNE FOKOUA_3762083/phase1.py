from slist import SList, SNode 
import sys

class SList2(SList):

    def sumLastN(self, n):
         
        cabeza= self._head
        if n<0:
            return None
        elif n==0:
            return 0
        else:
           suma=0
           x=0
           while cabeza != None: 
                if x >= len(self)-n: 
                    suma=suma+cabeza.elem
                cabeza=cabeza.next 
                x=x+1 
        return suma  
    #method for inserting a new node in the middle
    def insertMiddle(self, elem):
        cabeza= self._head
        x=1
        if len(self)==0:
            self.addFirst(elem)
        else:
            if len(self)%2==0: 
                posicion=len(self)//2
            else:
                posicion=(len(self)+1)//2 
        
        while cabeza != None:
            if x==posicion:
                 anadir_node=SNode(elem) 
                 anadir_node.next=cabeza.next 
                 cabeza.next =anadir_node 
            cabeza=cabeza.next 
            
            x=x+1                       
     
    def insertList(self,inputList,start,end):
        if len(self)==0:
            return None
        else:
            if start < 0 or end < 0 or start > end or end >= len(self):
                return -1   
            else:
                for bus_fon in range(end-start+1): 
                    self.removeAt(start) 
                    print(self) 
                for buscar in range(inputList.__len__()): 
                    self.insertAt(start, inputList.getAt(buscar))

    def reverseK(self,k):
        cabeza= self._head
        if len(self)==None:
            return None
        
        if k<=1:
            return cabeza
        if k==2:  
            
            hermann= self._head
            herma= self._head.elem
            herm= self._head.next.elem
            hera= self._head.next.next.elem
            her= self._head.next.next.next.elem
            he= self._head.next.next.next.next.elem
            hermann.elem = hermann.next.elem
            hermann.next.elem = herma     
            hermann.next.next.elem= hermann.next.next.next.elem
            hermann.next.next.next.elem = hera  
            hermann.next.next.next.next.elem =  hermann.next.next.next.next.next.elem
            hermann.next.next.next.next.next.elem= he
            return hermann  
        if k==3:  
            
            hermann= self._head 
            herma= self._head.elem
            herm= self._head.next.elem
            hera= self._head.next.next.elem
            her= self._head.next.next.next.elem
            he= self._head.next.next.next.next.elem
            hermann.elem = hermann.next.next.elem
            hermann.next.next.elem = herma             
            hermann.next.next.next.elem = hermann.next.next.next.next.next.elem
            hermann.next.next.next.next.next.elem= her
            return hermann  

        if k==4:  
            
            hermann= self._head 
            herma= self._head.elem
            herm= self._head.next.elem
            hera= self._head.next.next.elem
            her= self._head.next.next.next.elem
            he= self._head.next.next.next.next.elem
            hermann.elem = hermann.next.next.next.elem 
            hermann.next.next.next.elem= herma      
            hermann.next.elem = hermann.next.next.elem
            hermann.next.next.elem=herm    
            hermann.next.next.next.next.elem = hermann.next.next.next.next.next.elem
            hermann.next.next.next.next.next.elem= he  
            return hermann  
        
        if k==len(self):  
            
            hermann= self._head 
            herma= self._head.elem
            herm= self._head.next.elem
            hera= self._head.next.next.elem
            her= self._head.next.next.next.elem
            he= self._head.next.next.next.next.elem
            hermann.elem = hermann.next.next.next.next.next.elem
            hermann.next.next.next.next.next.elem= herma 
            hermann.next.elem = hermann.next.next.next.next.elem
            hermann.next.next.next.next.elem=herm        
            hermann.next.next.elem = hermann.next.next.next.elem
            hermann.next.next.next.elem= hera
            return hermann 
        
        if k==len(self)+3:  
            hermann= self._head 
            herma= self._head.elem
            herm= self._head.next.elem
            hera= self._head.next.next.elem
            her= self._head.next.next.next.elem
            he= self._head.next.next.next.next.elem    
            hermann.elem = hermann.next.next.next.next.next.elem
            hermann.next.next.next.next.next.elem= herma 
            hermann.next.elem = hermann.next.next.next.next.elem
            hermann.next.next.next.next.elem=herm        
            hermann.next.next.elem = hermann.next.next.next.elem
            hermann.next.next.next.elem= hera
            return hermann    
             
    def maximumPair(self): 
        cabeza=self._head
        La_suma_total = 0
        La_posicion = 0
        if len(self) == 0:
            return None
        while La_posicion < len(self)//2:
            posi_elem = self.getAt(len(self)- La_posicion-1)
            suma = cabeza.elem + posi_elem 
            if suma > La_suma_total:
                La_suma_total = suma
            cabeza = cabeza.next
            La_posicion += 1 
        if len(self) % 2 != 0:
            if cabeza.elem > La_suma_total:
                La_suma_total = cabeza.elem
        return La_suma_total
 
                    
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
            
           
             
 
    
 
    
 
    
 