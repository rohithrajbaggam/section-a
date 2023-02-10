# # from pprint import pprint
student = [ {
        "name" : "lucy",
        "age" : 21,
        "branch" : "CSE",
        "grade" : {
            "10th" : 90,
            "12th" : 88,
            "btech" : 85
        }
    },  {
        "name" : "max",
        "age" : 23,
        "branch" : "ME",
        "grade" : {
            "10th" : 92,
            "12th" : 86,
            "btech" : 84
        }
    }
]

for i in student:
    # print(i)
    for j in i:
        print(j, i[j])
    print()

# for i in student:
#     for j in i.keys():
#         print(j,i[j])
# student = {
#     1 : {
#         "name" : "lucy",
#         "age" : 21,
#         "branch" : "CSE",
#         "grade" : {
#             "10th" : 90,
#             "12th" : 88,
#             "btech" : 85
#         }
#     }, 
#     2 : {
#         "name" : "max",
#         "age" : 23,
#         "branch" : "ME",
#         "grade" : {
#             "10th" : 92,
#             "12th" : 86,
#             "btech" : 84
#         }
#     }
# }
# for i in student.keys():
#     # print(i)
#     for j in student[i].keys():
#         print(j, student[i][j])
#     print()
# for i in student.keys():
#     for j in student[i]:
#         print(j,student[i][j])
# pprint(student)
# print(student)
# student["university"] = "ABC University"
# print(student["name"])
# print(student.keys())

# for i in student.keys():
#     print(i, student[i])

# student = {
#     "name" : "lucy",
#     "age" : 21,
#     "branch" : "CSE"
# }

# # print(student["name"])
# # print(student.keys())

# for i in student.keys():
#     print(i, student[i])


