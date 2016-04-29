class PrimeChecker(object):
  
  def __init__(self,number):
    self.number = number
    
  def is_prime(self):

    prime = False
    
    if self.number == '':
      return prime

    if self.number < 2:
      return prime

    if self.number == 2:
      return True

  
    else:
      self.number = int (self.number)
      for i in range(2, self.number + 1):
        if self.number % i != 0:
          return True
          
        else:
          return False
    
try1 = PrimeChecker('67')
print try1.is_prime()   