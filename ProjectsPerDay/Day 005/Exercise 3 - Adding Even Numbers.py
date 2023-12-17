target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
s = 0
for n in range(2,target+1,2):
    s += n
print(s)
