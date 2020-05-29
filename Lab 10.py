#problem 2

def list_intersection(lst1,lst2):
  answer_list=[]
  my_dict={}
  for elem in lst1:
    my_dict[elem]=1
  for elem in lst2:
    if elem in my_dict:
      answer_list.append(elem)
    else:
      pass
  return answer_list

print(list_intersection([5,6,1,10],[8,1,6,9,5,3,8]))
      
#problem 3

def mode_of_list(lst):
  my_dict={}
  for elem in lst:
    if elem in my_dict:
      my_dict[elem]+=1
    else:
      my_dict[elem]=1

  largest_key=0
  largest_val=0
  for key in my_dict:
    if my_dict[key]>=largest_val:
      largest_val=my_dict[key]
      largest_key=key
    
  
  return largest_key

print(mode_of_list([1,3,2,1,2,1,2,2]))
print(mode_of_list([1,3,2,1,2,1,2,2,1,1,1,1]))


#Problem 4

def two_sum(lst,target):
  tuple_val=(None,None)
  my_dict={}
  for elem in lst:
    my_dict[elem]=1

  for elem in lst:
    val=target-elem
    if val in my_dict:
      tuple_val=(elem,val)

  return tuple(tuple_val)


print(two_sum([-5,2,8,-3,7,1],5))
print(two_sum([-5,2,8,-3,7,1],-1))


#Problem 5

def is_anagram(str1,str2):
  my_dict={}
  my_dict2={}
  for letter in str1:
    if letter not in my_dict:
      my_dict[letter]=1
    else:
      my_dict[letter]+=1

    
  for letter in str2:
    if letter not in my_dict2:
      my_dict2[letter]=1
    else:
      my_dict2[letter]+=1



  for key in my_dict:
    if key not in my_dict2:
      return False
    else:
      if my_dict[key]!=my_dict[key]:
        return False


  return True




    
      
print(is_anagram("angered","enraged"))
print(is_anagram("angeres","enraged"))
  
  
























