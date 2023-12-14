sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split(" ")
result = {w:len(w) for w in words}

print(result)

