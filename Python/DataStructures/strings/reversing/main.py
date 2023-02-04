string  = "mom"
rev_str = ""
# print(string)

# # print(string[::-1])

# print(string[::-1])
# print(string[3 : len(string)])

if string == string[::-1]:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")

# for i in range(len(string)-1, -1, -1):
#     # print(string[i])
#     rev_str += string[i]

# if string == rev_str:
#     print(f"{string} is palindrome")
# else:
#     print(f"{string} is not palindrome")