#Problem is: Circle of students
stored_values=[]
number_of_queries=int(input())
for i in range(number_of_queries):
  
  count=1 #variable that is just supposed to keep moving forward
  
  number_of_students=input()
  permutations_of_students=input().split()
  
  #converts the list of strings to a list of ints
  for i in range(len(permutations_of_students)):
    permutations_of_students[i]=int(permutations_of_students[i])
  one_starts_at=permutations_of_students.index(1)


  #checks if they are clock-wise or anti-clockwise
  variable_holder="YES"
  for i in range(len(number_of_students)-1):
    if not((one_starts_at+1)%len(permutations_of_students)==count+1):
      variable_holder="NO"
      one_starts_at+=1
    elif not((one_starts_at-1)%len(permutations_of_students)==count+1):
      variable_holder="NO"
      one_starts_at-=1

  stored_values.append(variable_holder)

for ch in stored_values:
  print(ch)
    

    
    
    
  
  
