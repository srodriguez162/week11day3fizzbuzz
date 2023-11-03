n = int(input("enter a number: "))
number = range(0,n+1)
for i in number:
  if i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")
  elif i % 5 == 0:
    print("buzz")
  elif i % 3 == 0:
    print("fizz")
  else:
    print(i)

