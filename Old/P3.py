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




def merge_linked_lists(srt_lnk_lst1,srt_lnk_lst2):
  
  def merge_sublists_helper(DoublyLL, node1,node2):

    #Defining base case, if we reach a point where both nodes are none; simply return 

    if (node1 is srt_lnk_lst1.trailer) and (node2 is srt_lnk_lst2.trailer):
      return DoublyLL

    #Defining recursive step

    else:
        
      #solve the function for the smaller input and pass the rest of the list into the helper function again till it reaches the end
        
      if (node1 is not srt_lnk_lst1.trailer) and (node2 is not srt_lnk_lst2.trailer):
          if node1.data<node2.data:
              DoublyLL.add_last(node1.data)
              DoublyLL.add_last(node2.data)
          else:
              DoublyLL.add_last(node2.data)
              DoublyLL.add_last(node1.data)
          return merge_sublists_helper(DoublyLL, node1.next, node2.next)
      elif node1 is not srt_lnk_lst1.trailer:
          while node1 is not srt_lnk_lst1.trailer:
            DoublyLL.add_last(node1.data)
            node1=node1.next
          return DoublyLL
      else:
          while node2 is not srt_lnk_lst2.trailer:
              DoublyLL.add_last(node2.data)
              node2=node2.next
          return DoublyLL

  if len(srt_lnk_lst1)>0 or len(srt_lnk_lst2)>0:
    DoublyLL=DoublyLinkedList()
    newDoublyLL=merge_sublists_helper(DoublyLL,srt_lnk_lst1.header.next,srt_lnk_lst2.header.next)
    return newDoublyLL
  else:
    return DoublyLinkedList()




