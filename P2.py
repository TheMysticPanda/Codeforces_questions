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

class Integer:

  def __init__(self, num_str):
    self.data=DoublyLinkedList()
    for char in num_str:
      self.data.add_last(int(char))

  def __add__(self, other):
    num_str=[]
    if_add_one=False
    self_curr_num=self.data.trailer.prev
    other_curr_num=other.data.trailer.prev

    #This part should calculate the sum of the number of digits of the smaller of the two numbers
    while (self_curr_num is not self.data.header) and (other_curr_num is not other.data.header):
      add_val_unit=self_curr_num.data+other_curr_num.data
      if if_add_one==True:
        add_val_unit+=1
      if add_val_unit>9:
        if_add_one=True
      else:
        if_add_one=False
      num_str.append(str(add_val_unit%10))
      self_curr_num=self_curr_num.prev
      other_curr_num=other_curr_num.prev


    #This part is to compute the rest of the sum
      
    if self_curr_num is self.data.header:
      while other_curr_num is not other.data.header:
        add_val_unit=other_curr_num.data
        if if_add_one==True:
          add_val_unit+=1
        if add_val_unit>9:
          if_add_one=True
        else:
          if_add_one=False
        num_str.append(str(add_val_unit%10))
        other_curr_num=other_curr_num.prev
    else:  
      while self_curr_num is not self.data.header:
        add_val_unit=self_curr_num.data
        if if_add_one==True:
          add_val_unit+=1
        if add_val_unit>9:
          if_add_one=True
        else:
          if_add_one=False
        num_str.append(str(add_val_unit%10))
        self_curr_num=self_curr_num.prev


    if if_add_one==True:
      num_str.append("1")

    num_str.reverse()

    #It is being converted to a string again because we need to return an Integer object
    input_int="".join(num_str)
    return Integer(input_int)
    

  def __repr__(self):
    int_val=[]
    for unit_num in self.data:
      int_val.append(str(unit_num))
    return "".join(int_val)
      








  
