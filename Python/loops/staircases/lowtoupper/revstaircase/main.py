n = int(input())

for i in range(n):
    # upper loop 
    for j in range(n-i-1):
        print(" ", end=" ")
    # lower loop 
    for k in range(i+1):
        print("*", end=" ")
    print()

