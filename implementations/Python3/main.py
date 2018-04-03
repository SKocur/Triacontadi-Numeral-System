def convertDecimalToTriacontadi(decimal):
  result = ""
  
  while True:
    num = str(decimal // 32)
    num_left = decimal - int(num) * 32
    
    if num_left < 10:
      result += str(num_left)
    else:
      result += chr(num_left + 55)
    
    if int(num) < 32:
      if int(num) < 10:
        result += num
      else:
        result += chr(int(num) + 55)
      break
    
    decimal = int(num)
  
  return result[::-1]
