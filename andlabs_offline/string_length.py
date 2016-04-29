def string_length(A):
  
  the_list_of_string_length = []
  
  if type(A) == str:
    length = len(A)
    the_list_of_string_length.append(length)
    return the_list_of_string_length
    
  elif type(A) == list:
    for i in A:
      length = len(i)
      the_list_of_string_length.append(length)
    return the_list_of_string_length
print string_length(['Michael', 'William', 'Smith'])