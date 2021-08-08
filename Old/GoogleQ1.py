def solution(A,B):
  listA=A.split(",")
  listB=B.split(",")
  
  answer_list=[]

  for i in range(len(listB)):
    letter=min(listB[i])              #while count and min could have been written in one for loop, their asymptotic running time remains the same
    listB[i]=listB[i].count(letter)
    
  for i in range(len(listA)):
    letter=min(listA[i])
    listA[i]=listA[i].count(letter)



  for numB in listB:
    count=0
    for numA in listA:
      if numA<numB:
        count+=1
    answer_list.append(count)

  return answer_list
    
    
    
    
    
