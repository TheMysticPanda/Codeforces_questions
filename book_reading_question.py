number_of_queries=int(input())

resulting_values=[]
bigger_list=[]

for i in range(number_of_queries):
  list_of_data=input().split()
  for i in range(2):
    list_of_data[i]=int(list_of_data[i])
  bigger_list.append(list_of_data)
    
  


for smaller_list in bigger_list:
  summation=0
  
  numberOfPages=int(smaller_list[0])
  RequiredDivisor=int(smaller_list[1])

  first_ten_last_digits=[None]*10

  for i in range(10):
    first_ten_last_digits[i]=(RequiredDivisor*(i+1))%10

  sum_last_digits=sum(first_ten_last_digits)
 
  
  numberoftimes=numberOfPages//RequiredDivisor

  summation+=((numberoftimes//10)*sum_last_digits)
  for i in range(numberoftimes%10):
    summation+=first_ten_last_digits[i]
  

  resulting_values.append(summation)


print(resulting_values)
    
    
  
  

  
  

  
  
