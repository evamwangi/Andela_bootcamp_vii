def reverse_string(string):
  
  length = len(string)
  the_list = []
  
  if length == 0:
    return None
    
  for i in range(length-1, -1, -1):
    
    the_list.append(string[i])
    string_made = "".join(the_list)
    
  if string_made == string:
    return string
    
  else:
    return string_made
