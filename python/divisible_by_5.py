def check_divisibility(num):
  # // Expected output is "TRUE" or "FALSE"
  if num % 5 ==0:
    print("it is divisible by 5")
  else:
    print("it is not divisible by 5")
  
  
num=int(input("Enter a number: "))
print(check_divisibility(num))
