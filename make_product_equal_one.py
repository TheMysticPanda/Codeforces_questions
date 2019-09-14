#make product equal to one

user_input=int(input())
list_of_ints=input().split()
for i in range(len(list_of_ints)):
  list_of_ints[i]=int(list_of_ints[i])

number_of_negatives=0
number_of_positives=0
number_of_zeroes=0
coins_needed=0

for i in range(len(list_of_ints)):
  if list_of_ints[i]<0:
    number_of_negatives+=1
    coins_needed+=((list_of_ints[i]*-1)-1)
  elif list_of_ints[i]>0:
    number_of_positives+=1
    coins_needed+=(list_of_ints[i]-1)
  else:
    number_of_zeroes+=1

#case when all inputs are either 1 or -1

if (number_of_zeroes==0):
  if (number_of_negatives%2)!=0:
    coins_needed+=2
else:
  coins_needed+=number_of_zeroes

print(coins_needed)

  
