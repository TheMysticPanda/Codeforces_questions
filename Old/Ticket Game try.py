import time

numberofnumbers= int(input())
input_value=input()


sum_first_half=0
sum_second_half=0

q1=0
q2=-1

for i in range(int(numberofnumbers/2)):
  try:
    sum_first_half+=int(input_value[i])
  except:
    q1+=1
    sum_first_half+=9

for i in range(int(numberofnumbers/2)):
  try:
    sum_second_half+=(int(input_value[(numberofnumbers/2)+i]))
  except:
    q2+=1





if q1%2!=0:  #bicarps'turn comes first in the second half
 if q2%2==0:  #monocarp gets last choice
   print("Monocarp")
 else: #bicarp gets last choice
    if 0<=sum_first_half-sum_second_half-(9*(q2-1))<=9:
     print("Bicarp")
    else:
      print("Monocarp")
   
else: #monocarp's turn in the second half
  if q2%2==0: #bicarp gets last choice
    if 0<=sum_first_half-sum_second_half-(9*(q2-1))<=9:
     print("Bicarp")
    else:
      print("Monocarp")
  else: #monocarp gets last choice
    print("Monocarp")
  

  
