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


file = open("numbers_1_million.txt", "w")
for i in range(1000000):
  file.write(str(i) + " " + convertDecimalToTriacontadi(i) + "\n")
file.close()

file = open("numbers_500_thousand.txt", "w")
for i in range(500000):
    file.write(str(i) + " " + convertDecimalToTriacontadi(i) + "\n")
file.close()

file = open("numbers_100_thousand.txt", "w")
for i in range(100000):
    file.write(str(i) + " " + convertDecimalToTriacontadi(i) + "\n")
file.close()