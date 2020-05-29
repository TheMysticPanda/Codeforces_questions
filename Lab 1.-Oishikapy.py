class Polynomial:

  def __init__(self, listcoefficients):
    self.listcoefficients= listcoefficients

  def __repr__(self):
    polynomialstringlist= []
    if self.listcoefficients[0] != 0:
      polynomialstringlist.append("+ "+str(self.listcoefficients[0]))
      for i in range(1,len(self.listcoefficients)):
        if self.listcoefficients[i]!=0:
          polynomialstringlist.append((str(self.listcoefficients[i])+"x^"+str(i)))
    polynomialstringlist.reverse()
    return " ".join(polynomialstringlist)
    
  def eval(self, val):
    amount=0
    for i in range(1,len(self.listcoefficients)):
      if self.listcoefficients[i] != 0:
        amount+=(val**i)*self.listcoefficients[i]
    if self.listcoefficients[0]!=0:
      amount+=self.listcoefficients[0]
    return amount
      
  def __add__(self,other):
    new_poly_list=[]
    new_poly_list.append(self.listcoefficients[0]+other.listcoefficients[0])
    smaller_list=min(len(self.listcoefficients),len(other.listcoefficients))
    for i in range(1,smaller_list):
      coeffs_new= self.listcoefficients[i] + other.listcoefficients[i]
      new_poly_list.append(coeffs_new)
    if len(self.listcoefficients)>smaller_list:
      new_poly_list.extend(self.listcoefficients[smaller_list:])
    else:
      new_poly_list.extend(other.listcoefficients[smaller_list:])
    return Polynomial(new_poly_list)
    
  def __mul__(self,other):
    new_poly_degrees=[]
    new_poly_coeffs=[]
    for i in range(0,len(self.listcoefficients)):
      for j in range(0,len(other.listcoefficients)):
        new_degrees= i+j
        new_coeffs= self.listcoefficients[i]*other.listcoefficients[j]
        if new_degrees in new_poly_degrees:
          index= new_poly_degrees.index(new_degrees)
          new_poly_coeffs[index]+=new_coeffs
        else:
          new_poly_degrees.append(new_degrees)
          new_poly_coeffs.append(new_coeffs)
    lenlist=[0]*max(new_poly_degrees)
    for i in range(len(new_poly_degrees)):
      lenlist.insert(new_poly_degrees[i],new_poly_coeffs[i])
    return Polynomial(lenlist)

  def polySequence(self,start, end, step = 1):
    for i in range(start,end,step):
      yield self.eval(i)
      
  
        
  def derivative(self):
    new_poly_coeffs=[]
    for i in range(1,len(self.listcoefficients)):
      new_coeff=i*self.listcoefficients[i]
      new_poly_coeffs.append(new_coeff)
    return Polynomial(new_poly_coeffs)

  
    
      
      
      




















        
          
