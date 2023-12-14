with open("file1.txt") as file1:
    data_file1 = file1.readlines()
    num_file1 = [int(n.strip()) for n in data_file1]

with open("file2.txt") as file2:
    data_file2 = file2.readlines()
    num_file2 = [int(n.strip()) for n in data_file2]

result = [n for n in num_file1 if n in num_file2]

# Write your code above 👆

print(result)


