n = int(input())
count = 0 

for i in range(1, n):
    if n%i == 0:
        print(i, end=", ")
        count+=1 
print()
if count == 1:

    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")


