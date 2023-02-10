
a = "abc"
try:
    print(int(a)) 
    print(a[5])
except Exception as e:
    print(f"Internal Server Error, {e}")
# try:
#     print(int(a)) 
#     print(a[5])
# except ValueError:
#     print("Only Integers are allowed for typecasting")
# except IndexError:
#     print("Index is out of range")
# print(int(a)) # ValueError
# print(a[5]) # IndexError