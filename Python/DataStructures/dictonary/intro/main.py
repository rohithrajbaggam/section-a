students = {
    1 : {
        "name" : "mike",
        "age" : 20,
        "gender" : "male",
        "grade" : {
        "10" : 92,
        "12" : 88,
        "B-Tech" : 85
        }
    },
    2 : {
        "name" : "lucy",
        "age" : 20,
        "gender" : "female",
        "grade" : {
        "10" : 93,
        "12" : 87,
        "B-Tech" : 84
        }
    }
}

for i in students.keys():
    # print(students[i])
    for j in students[i]:
        print(j, students[i][j])
    print()
    print()


# student  = {
#     "name" : "max",
#     "age" : 21,
#     "university" : "ABC University"
# }

# # print(student.keys())

# # print(student["name"])

# for i in student.keys():
#     print(i, student[i])


