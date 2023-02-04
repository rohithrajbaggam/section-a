

# def function(a, b=2):
#     print(a, b)

# function(a=1, b=2)
# function(b=1, a=2)
# function(1)


# mylist = [5,2, 4,1,3, 4]
# mylist.sort(reverse=True)
# print(mylist)

"""
user defined input
n = int(input("Enter size of list : "))

for i in range(n):
    x = input()
    mylist.append(x)

print(mylist)
"""


"""



def sort(mylist, reversed=False):
    for i in range(len(mylist)):
        # print(mylist)
        for j in range(len(mylist)):
            if reversed:
                if mylist[i] > mylist[j]:
                    mylist[i], mylist[j] = mylist[j], mylist[i]
            else:
                if mylist[i] < mylist[j]:
                    mylist[i], mylist[j] = mylist[j], mylist[i]
        

mylist = [5,2, 4,1,3, 4]
print(mylist)
sort(mylist)
print(mylist)
sort(mylist, reversed=True)
print(mylist)

"""