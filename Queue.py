class ArrayQueue:
  
  def __init__(self):
    self.data=[None]*8
    self.no_of_elems=0
    self.front_index=None

  def __len__(self):
    return self.no_of_elems

  def is_empty(self):
    return len(self)==0

  def enqueue_last(self,elem):
    if self.no_of_elems== len(self.data):
      self.resize(2*len(self.data))
    if self.is_empty():
      self.data[0]=elem
      self.front_index=0
      self.no_of_elems+=1
    else:
      back_ind=(self.front_index + self.no_of_elems)%len(self.data)
      self.data[back_ind]=elem
      self.no_of_elems+=1

  def enqueue_first(self,elem):
    if self.no_of_elems== len(self.data):
      self.resize(2*len(self.data))
    if self.is_empty():
      self.data[0]=elem
      self.front_index=0
      self.no_of_elems+=1
    else:
      self.front_index=(self.front_index - 1)%len(self.data)
      self.data[self.front_index]=elem
      self.no_of_elems+=1

  def dequeue_begin(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    elem=self.data[self.front_index]
    self.data[self.front_index]=None
    self.front_index = (self.front_index+1)%len(self.data) 
    self.no_of_elems-=1
    if self.is_empty():
      self.front_index=None
    elif len(self)<len(self.data)//4:   
      self.resize(len(self.data)//2)
    return elem

  def dequeue_last(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    back_ind=(self.front_index+self.no_of_elems-1)%len(self.data)
    elem=self.data[back_ind]
    self.data[back_ind]=None
    self.no_of_elems-=1
    if self.is_empty():
      self.front_index=None
    elif len(self)<len(self.data)//4:   
      self.resize(len(self.data)//2)
    return elem
    
  def resize(self, new_capacity):
    old_data = self.data
    self.data = [None] * new_capacity
    old_ind = self.front_index
    for new_ind in range(self.no_of_elems):
        self.data[new_ind] = old_data[old_ind]
        old_ind = (old_ind + 1) % len(old_data)
    self.front_index = 0

  def first(self):
      if self.is_empty():
          raise Exception("Queue is empty")
      return self.data[self.front_index]

  def last(self):
    if self.is_empty():
      raise Exception("Queue is empty")
    back_ind=(self.front_index+self.no_of_elems)%len(self.data)
    return self.data[back_ind]

class ArrayStack:
  def __init__(self):
    self.data=[]
  def __len__(self):
    return len(self.data)
  def is_empty(self):
    return (len(self)==0)
  def push(self,item):
    self.data.append(item)
  def pop(self):
    if self.is_empty()==True:
      raise Exception("Stack is empty")
    return self.data.pop()
  def top(self):
    if (self.is_empty()==True):
      raise Exception("Stack is empty")
    return self.data[-1]


def is_balances(expr):
  left-vl = "({["
  right-vl = ")}]"
  S = ArrayStack()
  for c in expr:
    if c in left-vl:
      S.push(c)
    elif c in right-vl:
      if S.is_empty( ):
        return False
      if right-vl.index(c) != left-vl.index(S.pop( )):
        return False
  return S.is_empty()


def get_expressions(input_str):
  start_ind=0
  start_ind = input_str.find("<", start_ind)
  end_ind = input_str.find(">", start_ind)
  while end_ind != -1:
    yield input_str[start_ind:end_ind+1]
    start_ind = input_str.find("<", end_ind+1)
    end_ind = input_str.find(">", end_ind+1)

 


def is1_matched(expr):
  gen=get_expressions(expr)
  S = ArrayStack()
  for elem in gen:
    if elem[1]!= "/":
      S.push(elem)
    else:
      if S.is_empty():
        return False
      S.pop()
  return S.is_empty()
      



















  






    
