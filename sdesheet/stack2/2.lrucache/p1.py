#1.So there could be get which just modifies the address and of course dll's links but you have to delte here too.
#2.Wheras for put if size is not reached just put it in and add it to the map
#But if size is reached then remove it from the ll and the map also and do the addition/

m={"hi":4,"k":4}
del m["hi"]
print(m)

class LRUCache:
    class Node:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.next=None
            self.prev=None

    def __init__(self, capacity: int):
        self.cap=capacity
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.m={}
        
    def add_node(self,new_node):
        
        #have to get those OTHER nodes first , head is anyways fine - direct i mean
        temp=self.head.next
        
        #change the one #YEHHHHHH
        new_node.next=temp
        new_node.prev=self.head
        
        #change the others 
        self.head.next=new_node
        temp.prev=new_node
        
        
    def delete_node(self,node):
        
        #have to get thoseOTHER  nodes first 
        prev_node=node.prev
        next_node=node.next
        
       
        #change the others 
        prev_node.next=next_node
        next_node.prev=prev_node
        
    def get(self, key: int) -> int:
        if key in self.m: #present in hashmap we have to check           
           
            res_node=self.m[key] 
            self.delete_node(res_node)
            self.add_node(res_node)
            
            #to return value no other reason.
            res=self.m[key].value
         
            
            #new address
            self.m[key]=self.head.next
            
            return res
           
            
        return -1   
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.delete_node(self.m[key])
            del self.m[key] #Rhis just for unifoormity in the code.

        if self.cap == len(self.m):
            del self.m[self.tail.prev.key]
            self.delete_node(self.tail.prev)

        new = self.Node(key, value)
        self.add_node(new)
        self.m[key] = new
        
        