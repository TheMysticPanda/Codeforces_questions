inputvalue=input()
inputvalues=input()
limit= int(inputvalue.split()[1])
listofelems=inputvalues.split()
counter=0
numofval=0
index=0
while (not (counter > limit)) and index<len(listofelems):
    counter+=int(listofelems[index])
    if counter<=limit:
      numofval+=1
      index+=1
    else:
      break

print(numofval)

