# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/(height**2))
if BMI < 18.5:
    print('Your BMI is ' + str(BMI) + ', you are underweight.')
elif (BMI >= 18.5) & (BMI < 25):
    print('Your BMI is ' + str(BMI) + ', you have a normal weight.')
elif (BMI >= 25) & (BMI < 30):
    print('Your BMI is ' + str(BMI) + ', you are slightly overweight.')
elif (BMI >= 30) & (BMI < 35):
    print('Your BMI is ' + str(BMI) + ', you are obese.')
elif BMI >= 35:
    print('Your BMI is ' + str(BMI) + ', you are clinically obese.')