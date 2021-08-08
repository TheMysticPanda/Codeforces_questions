#Problem is: Circle of students
stored_values=[]
number_of_queries=int(input())
for i in range(number_of_queries):
    
  number_of_students=int(input())
  permutations_of_students=input().split()
  
  #converts the list of strings to a list of ints
  for i in range(number_of_students):
    permutations_of_students[i]=int(permutations_of_students[i])
    
  one_starts_at=permutations_of_students.index(1)


  #checks if they are clock-wise or anti-clockwise
  forward_works = "YES"
  backward_works = "YES"

  for i in range(number_of_students - 1):
      forward_index = (one_starts_at+i+1)%number_of_students
      backward_index = (one_starts_at-i-1)%number_of_students
      if not(permutations_of_students[forward_index]==i+2):
        forward_works="NO"
      if not(permutations_of_students[backward_index]==i+2):
        backward_works="NO"

  if (forward_works == "YES" or backward_works == "YES"):
    print ("YES")
  else:
    print ("NO")
    

    
    
    
  
  
