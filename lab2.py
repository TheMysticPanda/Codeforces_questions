def find_first(input_lst):
  start_val=0
  end_val=len(input_lst)
  mid_point=(start_val+end_val)//2
  while end_val-start_val>1:
      if input_lst[mid_point]==1:
        end_val=mid_point
        mid_point=(start_val+end_val)//2
        answer_val=mid_point
      else:
        start_val=mid_point
        mid_point=(start_val+end_val)//2
        answer_val=mid_point
  return (answer_val+1)


def compute_e(n):
  product=1
  sumval=1
  for i in range(1,n+1):
    product*=(1/i)
    sumval+=product
  return sumval


def two_sum(sorted_lst,target):
  j=-1
  i=0
  while j<i:
      if sorted_lst[i]+sorted_lst[j]>target:
        j-=1
      elif sorted_lst[i]+sorted_lst[j]<target:
        i+=1
      elif sorted_lst[i]+sorted_lst[j]==target:
        return (sorted_lst[i],sorted_lst[j])
  return None

        

def seperate_neg_pos(lst):
  i=0
  j=len(lst)-1
  while i<j:
    if lst[i]<0:
      i+=1
    if lst[j]>0:
      j-=1
    if lst[i]>0 and lst[j]<0 and i<j:
      a=lst[i]
      lst[i]=lst[j]
      lst[j]=a
  return lst

def move_zeroes(lst):
  i=0
  for k in range(len(lst)):
    if lst[k]!=0:
      lst[i]=lst[k]
      i+=1
  for k in range(i,len(lst)):
    lst[k]=0
  return lst
    


def find_min(lst):
  if len(lst)==0:
    return None
  if len(lst)==1:
    return lst[0]
  else:
    val=find_min(lst[1:])
    answer=min(val,lst[0])
    return answer








  
  
