string = "a1b2c3d4e5f6g7h8"

# print(string.replace("d", "x"))
# print(string.capitalize())
# print(string.count("a"))
# print(string.isalpha())


alpha, num = "", ""

for i in string:
    if i.isdigit():
        num += i 
    else:
        alpha += i 
print(int(num), alpha)
