student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas
student_dataframe = pandas.DataFrame(student_dict)

# # Looping through a dataframe
# for (key,value) in student_dataframe.items():
#     print(key)
#     print(value)

# Looping through a row of a dataframe
for (index, row) in student_dataframe.iterrows():
    print(row.student)
    print(row.score)