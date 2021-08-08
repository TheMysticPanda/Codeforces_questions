def solution(N,K):
  possible_subarray=[]
  i=0
  while i+K<=len(N):
    if (N[i:i+K]) > possible_subarray:
      possible_subarray=N[i:i+K]
    i+=1

  return possible_subarray


    
