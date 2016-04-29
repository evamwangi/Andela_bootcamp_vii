def data_type(A):
  
  if type(A) == str:
    return len(A)
    
  elif A == None:
    return "no value"
    
  elif type(A) == bool:
    return A
    
  elif type(A) == int:
    if A > 100:
      return "more than 100"
      
    elif A < 100:
      return "less than 100"
      
    else:
      return "equal to 100"
      
  elif type(A) == list:
    if len(A) >= 3:
      return A[2]
    else:
      return None
print data_type(30)