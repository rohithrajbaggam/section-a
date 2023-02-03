# check n is palindrome

n = int(input())
temp = n 
_sum = 0

while n>0:
    rem = n%10 
    _sum = _sum*10 + rem 
    n = int(n/10)


if temp == _sum:
    print(f"{_sum} is palindrome")
else:
    print(f"{_sum} is not palindrome")

# reverse a number
# n = int(input())
# _sum = 0

# while n>0:
#     rem = n%10 
#     _sum = _sum*10 + rem 
#     n = int(n/10)

# print(_sum)



