import string

def conv(arg):
  intCount = 0
  punCount = 0
  
  for x in arg:
    if x in string.digits:
      intCount += 1
    elif x == '.':
      punCount += 1
    else:
      pass
      
  if intCount == len(arg):
    arg = int(arg)
  elif intCount == len(arg)-1 and punCount == 1:
    arg = float(arg)
  else:
    arg = str(arg)
    
  return arg
