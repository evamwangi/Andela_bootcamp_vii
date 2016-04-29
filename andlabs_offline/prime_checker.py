class PrimeChecker(object):
  
  def __init__(self,number = None):
    self.number = number
    
  def is_prime(self):
"""
takes a string e.g '43'
if it is a prime number it returns True
if it is not a prime number it returns False
if the string is empty it returns False
"""
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