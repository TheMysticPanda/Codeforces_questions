def binary_search_recurse(lst,val,low,high):
  midval=low+high//2
  if lst[midval]==val:
    return midval
  elif val<lst[midval]:
    val=binary_search_recurse(lst,val,low,midval)
    return val
  else:
    val=binary_search_recurse(lst,val,midval+1,high)
    return val



    
def nested_list_sum(lst):
  sumval=0 ##Can we use try and except?
  for elem in lst:
    if type(elem)==int:
      sumval+=elem
    else:
      val=nested_list_sum(elem)
      sumval+=val
  return sumval
  
      
def selection_sort(lst):
  for i in range(len(lst)):
    minval=lst[i]
    for j in range(i,len(lst)):
      if lst[j]<minval:
        lst[j],lst[i]=lst[i],lst[j]
  return lst
      


def selection_sort_recursive(lst,low,high):
  index_pos=low
  minval=lst[low]
  if low==high:
    return None
  for i in range(low,high+1):
    if lst[i]<minval:
      minval=lst[i]
      index_pos=i
  lst[low],lst[index_pos]=lst[index_pos],lst[low]
  selection_sort_recursive(lst,low+1,high)
  return lst
  
def quicksort(lst,start,end):
  i=start
  j=end
  if end-start<=0:
    return None
  while i!=j:
    if lst[j]<lst[i] and i<j:
      lst[i],lst[j]=lst[j],lst[i]
      i,j=j,i
    if j<i:
      j+=1
    if lst[j]>lst[i] and i>j:
      lst[j],lst[i]=lst[i],lst[j]
      i,j=j,i
    if j>i:
      j-=1
  quicksort(lst,start,i)
  quicksort(lst,i+1,end)
  return lst
  























  












