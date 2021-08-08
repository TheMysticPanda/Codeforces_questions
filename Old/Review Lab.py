def partition_lst(lst):
  i=0
  j=len(lst)-1
  while j<len(lst):
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
    if i==j:
      break
  return lst


def recurse_main(stringval,low,high):
  if low>high:
    return True
  else:
    a=recurse_main(stringval,low+1,high-1)
    b=(stringval[low]==stringval[high])
  return (a and b)

    




def give_index(base,n):
  for i in range(1,n+1):
    yield (base**i)


import random
def random_str_join(n):
  newlist=[0]*n
  letters="abcdefghijklmnopqrstuvwxyz"
  for i in range(n):
    a=letters[random.randint(0,len(letters)-1)]
    newlist[i]=a
  return " ".join(newlist)
