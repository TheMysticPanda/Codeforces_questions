#Problem 1
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None
            
    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def add_first(self, data):
        self.add_after(self.header, data)

    def add_last(self, data):
        self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        self.add_after(self.node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        node.disconnect()
        self.size -= 1
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.first_node()
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next

    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) + ']'



class LinkedStack:
  

  def __init__(self):
    self.data=DoublyLinkedList()


  def __len__(self):
    return len(self.data)


  def is_empty(self):
    return len(self.data)==0


  def push(self,value):
    if self.data.is_empty():
      self.data.add_first(value)
    else:
      self.data.add_after(self.data.trailer.prev,value)
      

  def pop(self):
    val=self.data.delete_node(self.data.trailer.prev)
    return val.data


  def top(self):
    val=self.data.trailer.prev.data
    return val.data

#Problem 2
  
class LeakyStackArray():
  def __init__(self,capacity):
    self.stack=[None]*capacity
    self.numofelems=0
    self.back_ind=None
    self.capacity=capacity

  def __len__(self):
    return self.numofelems

  def is_empty(self):
    return self.numofelems==0

  def push(self,value):
    if self.is_empty():
      self.stack[0]=value
      self.back_ind=0
      self.numofelems+=1
    elif self.numofelems==len(self.stack):
      front_index=(self.back_ind+self.numofelems)%self.capacity
      self.stack[front_index]=value
      self.back_ind=(self.back_ind+1)%self.capacity
    else:
      front_index=(self.back_ind+self.numofelems)%self.capacity
      self.stack[front_index]=value
      self.numofelems+=1
    
      
  def top(self):
      top_index=((self.back_ind+self.numofelems)%self.capacity)-1
      return self.stack[top_index]

  def pop(self):
    top_index=((self.back_ind+self.numofelems)%self.capacity)-1
    elem=self.stack[top_index]
    self.stack[top_index]=None
    self.numofelems-=1
    return elem

#Part b

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def add_first(self, data):
        self.add_after(self.header, data)

    def add_last(self, data):
        self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        node.disconnect()
        self.size -= 1
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.first_node()
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next

    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) + ']'



class LinkedLeakyStack:

    def __init__(self,capacity):
        self.data=DoublyLinkedList()
        self.capacity=capacity

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self,value):
        if len(self.data)<self.capacity:
            self.data.add_before(self.data.trailer,value)
        else:
            self.data.delete_node(self.data.header.next)
            self.data.add_before(self.data.trailer,value)
            
    def top(self):
        node=self.data.trailer.prev
        return node.data
            
    def pop(self):
        node=self.data.trailer.prev
        elem=node.data
        self.data.delete_node(node)
        return elem

#Problem 3

class ArrayQueue:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None

    # O(1) time
    def __len__(self):
        return self.num_of_elems

    # O(1) time
    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        # If number of elements == capacity (we've filled the list completely), resize
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
            

        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0

        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
        self.num_of_elems += 1


    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem

    # O(1) running time
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_capacity):
        
        old_data = self.data
        self.data = [None] * new_capacity
        
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
        


class QStack:

  def __init__(self):
    self.data=ArrayQueue()


  def __len__(self):
    return len(self.data)
    

  def is_empty(self):
    return len(self.data)==0

#Enqueue takes amortized O(1) time. Therefore, function takes O(1) time amortised. Worst case could be O(n) if resize is done. 
  def push(self,value):
    self.data.enqueue(value)
#Enqueue and dequeue takes amortized O(1) time. Therefore, function takes O(1) time amortised. Worst case could be O(n) if resize is done. 


  def pop(self):
    for i in range(len(self)-1):
      val=self.data.dequeue()
      self.data.enqueue(val)
    lastelem=self.data.dequeue()
    return lastelem
    
  def top(self):
    for i in range(len(self)-1):
      val=self.data.dequeue()
      self.data.enqueue(val)
    lastelem=self.data.dequeue()
    self.data.enqueue(lastelem)
    return lastelem
    

























  
    
