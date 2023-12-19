for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # use and (not or)
    print("FizzBuzz")
  elif number % 3 == 0: # use elif (not if)
    print("Fizz")
  elif number % 5 == 0: # use elif (not if)
    print("Buzz")
  else:
    print(number) # remove square brackets []